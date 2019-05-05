# Obzidi4n was here
from bs4 import BeautifulSoup
import cloudscraper, csv, re, requests, shutil

pluginFile = open('config/pluginurls.csv')
pluginReader = csv.reader(pluginFile)
pluginData = list(pluginReader)
pluginNum = pluginReader.line_num
manualPluginList = 'Manual Plugins:\n'

# command: update all
for i in range(1, pluginNum):

	pluginName = pluginData[i][0]
	pluginUrl = pluginData[i][2]

	print("Processing",i,"of",pluginNum,":",pluginName)

	# check if spigot
	if pluginData[i][1] == 'spigot':

		# invoke cloudscraper
		print ('Source: Spigot')
		scraper = cloudscraper.create_scraper()

		# get spigot page
		pluginApi = pluginUrl + '/history'
		r_page = scraper.get(pluginApi)

		# parse download link with BeautifulSoup
		soup = BeautifulSoup(r_page.text, 'html.parser')
		soup2 = soup.find('a', 'secondaryContent')
		target = 'http://www.spigotmc.org/' + soup2['href']

		# get response object
		r = scraper.get(target, stream=True) #, verify="/etc/ssl/certs/ca-certificates.crt")

		# get filename from pluginName
		fileName = pluginName + '.jar'

		# report
		print('Target:', target)
		print('File: ', fileName)

		# stream / save file
		with open('common-files/plugins/%s' % fileName, 'wb') as fd:
			for chunk in r.iter_content(chunk_size=128):
				fd.write(chunk)
		del r

		print('Saved \n\n')

	# check if jenkins
	elif pluginData[i][1] == 'jenkins':

		pluginApi = pluginUrl + '/lastStableBuild/api/xml'
		r_page = requests.get(pluginApi, verify=False)
		soup = BeautifulSoup(r_page.text, 'html.parser')

		# loop through all relativepaths
		for tag in soup.find_all('artifact'):

			# download
			fileName = tag.filename.string
			target = pluginUrl + '/lastStableBuild/artifact/' + tag.relativepath.string

			r = requests.get(target, stream=True) #, verify="/etc/ssl/certs/ca-certificates.crt")

			# report
			print('Plugin:', pluginName)
			print('Target:', target)
			print('File: ', fileName)

			 # stream / save file
			with open('common-files/plugins/%s' % fileName, 'wb') as fd:
				for chunk in r.iter_content(chunk_size=128):
					fd.write(chunk)
			del r
			
			print('Saved \n\n')

	# check if enginehub
	elif pluginData[i][1] == 'enginehub':

		# get page
		pluginApi = pluginUrl
		r_page = requests.get(pluginApi)

		# parse download link with BeautifulSoup
		soup = BeautifulSoup(r_page.text, 'html.parser')
		soup2 = soup.find(class_="col-md-8")
		soup3 = soup2.find('a')
		target = soup3['href']

		r = requests.get(target, stream=True) #, verify="/etc/ssl/certs/ca-certificates.crt")
		fileName = pluginName + '.jar'

		# report
		print('Plugin:', pluginName)
		print('Target:', target)
		print('File: ', fileName)

		# stream / save file
		with open('common-files/plugins/%s' % fileName, 'wb') as fd:
			for chunk in r.iter_content(chunk_size=128):
				fd.write(chunk)
		del r

		print('Saved \n\n')

	# check if static
	elif pluginData[i][1] == 'static':

		target = pluginUrl
		fileName = pluginName + '.jar'
		r = requests.get(target, stream=True) #, verify="/etc/ssl/certs/ca-certificates.crt")

		# report
		print('Plugin:', pluginName)
		print('Target:', target)
		print('File: ', fileName)

		# stream / save file
		with open('common-files/plugins/%s' % fileName, 'wb') as fd:
			for chunk in r.iter_content(chunk_size=128):
				fd.write(chunk)
		del r

		print('Saved \n\n')

	# check if manual
	elif pluginData[i][1] == 'manual':

		manualPluginList += pluginName
		manualPluginList += '\n'

		# report
		print('Plugin:', pluginName)
		print('Skipped for manual installation \n')

	# else error
	else:
		print('error updating', pluginName, ', please check the CSV file.')

# print list of manual plugins
print(manualPluginList)
