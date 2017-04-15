# bungee-server-script
This is a simple set of scripts for managing a Bungeecord network of Minecraft servers.

A set of basic tools to save the busy Minecraft admin a ton of time on routine tasks, including:

- Firing up and shutting down servers in tabs of a Tmux session.
- Automatically fetching the latest builds of plugins and replacing across the network.  
- Updating Spigot via Buildtools in a Tmux session, and replacing across the network.
- Updating Bungeecord
- Mirroring a server's configs into a Test server, great for testing plugin updates before going live.
- And much more ..

# Getting Started

This is built for a linux server environment - check the dependencies below and make sure you have everything.

Then, fire up **./mc help** for available commands.

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
