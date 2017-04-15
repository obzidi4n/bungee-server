# bungee-server-script
This is a simple set of scripts for managing a Bungeecord network of Minecraft servers.

A set of basic tools to save the busy Minecraft admin a ton of time on routine tasks:

- Fire up and shut down servers in tabs of a Tmux session.
- Automatically fetch the latest plugin builds from Spigot, Jenkins, Bukkit, etc. and replace them across the network.  
- Update Spigot and Bungeecord with simple commands.
- Run backups of your servers and send them to a cloud provider of your choice.
- Mirror any server's plugins and configs into a test environment.
- And much more ..

# Getting Started

This is built for a linux server environment - check the dependencies below and make sure you have everything.

Then, fire up **./mc help** for available commands.

** Quickstart **

1. Add your server's name and memory allocation to /config/serverlist
2. Build Spigot **./mc update spigot** and **./mc update spigotjars**
3. Get Bungee **./mc update bungee**
4. Generate Configs **./mc start bungee** and **./mc start <servername>**
5. Stop Servers **./mc stop bungee** and **./mc stop <servername>**
6. Adjust your configurations, ports, firewall etc.
7. Start Servers **./mc start bungee** and **./mc start <servername>**
8. Go to Console **./mc console**

# Questions?

Documentation and error-handling is being improved, but right now everything here 'just works'.   If you find any major bugs or have suggestions, please create an Issue above (or fork it).

# Dependencies:

- Tmux
- Python 3.x
- Zip
- Rsync

- Python libraries (use pip to install)
  - BeautifulSoup
  - requests
  - shutil
  - cfscrape

apt-get update
apt-get install python-pip zip default-jre zip 
pip install BS4 requests cfscrape
