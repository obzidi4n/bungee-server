from bs4 import BeautifulSoup
import csv
import re
import requests
import shutil
import cfscrape

pluginFile = open('config/pluginurls.csv')
pluginReader = csv.reader(pluginFile)
pluginData = list(pluginReader)
pluginNum = pluginReader.line_num

print(str(pluginNum-1), 'plugins')

# command: update all
for i in range(1, pluginNum):

    pluginName = pluginData[i][0]
    pluginUrl = pluginData[i][2]

    print (str(pluginNum-1), pluginName)

    # check if spigot
    if pluginData[i][1] == 'spigot':

	#invoke CloudflareScraper
	print ('Source: Spigot')
	scraper = cfscrape.create_scraper()

        # get spigot page
        pluginApi = pluginUrl + '/history'
        r = scraper.get(pluginApi)

        # parse download link with BeautifulSoup
        soup = BeautifulSoup(r.text, 'html.parser')
        soup2 = soup.find('a', 'secondaryContent')
        target = 'http://www.spigotmc.org/' + soup2['href']

        # get response object
        response = scraper.get(target, stream=True, verify=False)

        # get filename from header, or use pluginName
        try:
            d = response.headers['content-disposition']
            f = re.search('filename=\"(.+)\"', d)
            fileName = f.group(1)
        except KeyError:
            fileName = pluginName + '.jar'  # this presumes it's a jar, of course..

        # report
        print('Target:', target)
        print('File: ', fileName, '\n')

        # stream / save file
        with open('common-files/plugins/%s' % fileName, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

	print('Saved \n\n')

    # check if jenkins
    elif pluginData[i][1] == 'jenkins':

        pluginApi = pluginUrl + '/lastStableBuild/api/xml'
        r = requests.get(pluginApi, verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')

        # loop through all relativepaths
        for tag in soup.find_all('artifact'):

            # download
            fileName = tag.filename.string
            target = pluginUrl + '/lastStableBuild/artifact/' + tag.relativepath.string

            response = requests.get(target, stream=True, verify=False)

            # report
            print('Plugin:', pluginName)
            print('Target:', target)
            print('File: ', fileName, '\n')

            # stream / save file
            with open('common-files/plugins/%s' % fileName, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

	    print('Saved \n\n')

    # check if enginehub
    elif pluginData[i][1] == 'enginehub':

        # get page
        pluginApi = pluginUrl
        r = requests.get(pluginApi)

        # parse download link with BeautifulSoup
        soup = BeautifulSoup(r.text, 'html.parser')
        soup2 = soup.find(class_="col-md-8")
        soup3 = soup2.find('a')
        target = soup3['href']

        response = requests.get(target, stream=True, verify=False)
        fileName = pluginName + '.jar'

        # report
        print('Plugin:', pluginName)
        print('Target:', target)
        print('File: ', fileName, '\n')

        # save file
        with open('common-files/plugins/%s' % fileName, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

        print('Saved \n\n')

    # check if static
    elif pluginData[i][1] == 'static':

        target = pluginUrl
        fileName = pluginName + '.jar'
        response = requests.get(target, stream=True, verify=False)

        # report
        print('Plugin:', pluginName)
        print('Target:', target)
        print('File: ', fileName, '\n')

        # save file
        with open('common-files/plugins/%s' % fileName, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

        print('Saved \n\n')

    # else error
    else:
        print('error updating', pluginName, ', please check the CSV file.')
