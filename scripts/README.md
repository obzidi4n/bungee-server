This is where the fun stuff is.  

**Plugins.py** gets called by the **./mc update plugins** command, and handles all the negotiation with various services to identify and download the latest version (works with Bukkit, Spigot, Jenkins, Enginehub, or static URLs).  It pulls info from **bungee-server/config/pluginurls.csv**.   Edit your plugin info there.

**Pluginnuke.py** can be called manually from the shell to hunt down and delete specified plugins across your network.  Be careful.

**Pluginrename.py** can be called manually from the shell to hunt down and rename specified plugins across your network.
