# GSMS
## Game Server Management System
--- 

**These files are currently under changes and the information below is subject to change and may no longer be accurate.**

### Installation 
**Up to date version:**  
PIP: `pip install --upgrade https://github.com/Pukeko-Host/GSMS/tarball/master`  
**Development version:**  
PIP: `pip install --upgrade https://github.com/Pukeko-Host/GSMS/tarball/development`  

### Importing
`From GSMS import GSMS`  
  
**You should never have any need to directly import `GS.py` from `GSMS` as the `GameServer` class is already imported from `GS.py` by `GSMS.py`.**  

### Information
 - GSMS.py - manages `GameServer` children by communicating with the mother server and performing operations based off instructions. Operates within a VPS (Debian 10) with an expected average of 4 servers under it's management at a time.  
  Usage:  
    - `resume_servers()` will contact the mother server about any servers it should be running in case of any outage, will restart all accordingly and then will return a `dict` of all running `GameServer`s, empty if none.
    - `start_server(user_id, game_id, gameservers)` will start a game server of the game that corresponds with `game_id` and add it to `gameservers`.
    - `stop_server(gameserver_id, gameservers)` will stop a server that corresponds with `gameserver_id` and will remove it from `gameservers`.


- GS.py - contains `GameServer` object, this is responsible for opening the server executable and interacting with its stdin and stdout.  
  Definition: `GameServer([args])` args being the input on the command line  
  Example: `GameServer(["TerrariaServer.exe"])` or `GameServer(["TerrariaServer.exe", "-steam"])`  
  Usage:
  - `GameServer().start()` to start stdout recording thread and run args in the command line to start the server process.
  - `GameServer().stop()`will stop the server process and close stdin and stdout.
  - `GameServer().send_input(input)` sends input to stdin.
  - The stdout can be accessed from `GameServer().stdout_output`, a list containing all lines from stdout.   
-   GSMS.py - an instance of this will be running on every VPS, managing the `GameServers` on it.

- File structure:  
  - **Server files:** `/opt/pukeko/gsms/{game}/` 
  Files like server.jar or TerrariaServer.bin.x86_64 would be stored here. As only one local copy of then is needed.
  - **World files:** `~/.pukeko/gsms/{game}/{server_id}/`  
  Files like terraria_world.wld would be stored here, other games might have clunkier versions with shortcuts or actual copies of the server binary/jar inside them though.
  - **World backups:** `~/.pukeko/gsms/{game}/{server_id}/backups/`  
  Compressed world folders/files will be stored here.
  
