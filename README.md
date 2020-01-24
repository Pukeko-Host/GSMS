# GSMS
--- 
### Game Server Management System and Game Servers
 
- gameservers.py - contains `GameServer` object, this is responsible for opening the server executable and interacting with its stdin and stdout.  
  Definition: `GameServer([args])` args being the input on the command line  
  Example: `GameServer(["TerrariaServer.exe"])` or `GameServer(["TerrariaServer.exe", "-steam"])`  
  Usage:
  - `GameServer().start()` to start stdout recording thread and run args in the command line to start the server process.
  - `GameServer().stop()`will stop the server process and close stdin and stdout.
  - `GameServer().send_input(input)` sends input to stdin.
  - The stdout can be accessed from `GameServer().stdout_output`, a list containing all lines from stdout.   
-   GSMS.py - an instance of this will be running on every VPS, managing the `GameServers` on it.


