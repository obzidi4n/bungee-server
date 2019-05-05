# Bungeecord / Spigot Server Wrapper for Minecraft
A simple server wrapper setup for linux using Tmux, plus some helpful scripts that will save you tons of time on routine admin tasks:

- Automatically fetch the latest plugin builds from Spigot, Jenkins, Bukkit, etc. and replace them across the network.  
- Update Spigot and Bungeecord with simple commands.
- Fire up and shut down servers in tabs of a Tmux session.
- Run backups of your servers and send them to a cloud provider of your choice.
- Mirror any server's plugins and configs into a test environment.
- And much more ..

# Getting Started

This is built for a linux environment - check the dependencies below and make sure you have everything.

Then, fire up **./mc help** for available commands.

** Quickstart **

1. Add your server's name and memory allocation to **/config/serverlist**
2. Build Spigot **./mc update spigot** (.. wait for build, then) **./mc update spigotjars**
3. Get Bungee **./mc update bungee**
4. Drop in valid EULAs **./mc update eula**
5. Generate Configs **./mc start bungee** and **./mc start ServerName**
6. Stop Servers **./mc stop bungee** and **./mc stop ServerName**
7. Adjust your configurations, ports, firewall etc.
8. Start Servers **./mc start bungee** and **./mc start ServerName**
9. Go to Console **./mc console**

# Questions?

Documentation and error-handling is being improved, but right now everything here 'just works'.   If you find any major bugs or have suggestions, please create an Issue above (or fork it).

Need a simple Tmux config?  May we suggest [Obzidi4n's Stupid Simple Tmux.conf](https://github.com/obzidi4n/tmux.conf).

# Dependencies:

- Tmux
- Python 3.x
- Zip
- Rsync
- Nodejs

- Python libraries 
  - BeautifulSoup
  - cloudscraper

`apt-get update`

`apt-get install nodejs python3 python3-pip rsync tmux zip`

`pip3 install beautifulsoup4 cloudscraper`
