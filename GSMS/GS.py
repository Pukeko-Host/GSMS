"""
GameServer classes that operate dedicated server executables
Managed by GSMS.py
Requires to be run on POSIX OSes (Tested and designed for Linux VPS machines)
"""

from pty import openpty
from subprocess import Popen, PIPE, TimeoutExpired
from threading import Thread

import time

def get_server_folder(game, version=None):
    output = f"/opt/pukeko/gsms/{game}/" 
    if version:
        output += str(version) + "/"
    return output

def get_world_folder(game, server_id):
    return f"~/.pukeko/gsms/{game}/{server_id}/"

class GameServer:
    """
    Object for handling server processes in the terminal
    """
    def __init__(self, server_id):
        self.stdout_output  = []
        self.stdout_handle  = None
        self.stdin_handle   = None
        self.process        = None
        self.args           = None
        # Unique identifying string ID for this GS, used for folder storage and screen names
        self.server_id = str(server_id)
        # https://docs.python.org/3/library/threading.html#thread-objects
        self.thread         = Thread(target=self._record_output, daemon = True)

    def first_time_setup():
        raise NotImplementedError("This GS either does not need to perform first time setup, or it has not been implemented yet.")

    def _record_output(self):
        for line in iter(self.stdout_handle.readline, b''):
            self.stdout_output.append(line)
        self.stdout_handle.close()

    def send_input(self, stdin_input):
        if self.stdin_handle is not None:
            self.stdin_handle.write(f"{stdin_input.rstrip()}\n") # Send byte string to stdin
            self.stdin_handle.flush() # Clear stdin buffer
   
    def _start_server(self):
        """
        Creates a Popen object running self.args as stdin, stdout and stderr sent to PIPE
        (Use the GameServer.send_input() method to access stdin, do not attempt to access stderr or stdout)
        https://docs.python.org/3/library/subprocess.html#popen-objects
        """
        # Creating psuedo-terminal pair https://docs.python.org/3/library/pty.html#pty.openpty
        master, slave = openpty()
        # Creating process of executable https://docs.python.org/3/library/subprocess.html#subprocess.Popen
        self.process = Popen(["screen", "-S", self.server_id] + self.args, stdin=PIPE, stdout=slave, close_fds=True, universal_newlines=True)
        self.stdin_handle = self.process.stdin # Use stdin_handle for interactions with the stdin of process
        self.stdout_handle = open(master) # Use stdout_handle for reading the stdout of process

    def start(self):
        # Start server
        self._start_server()
        self.thread.start() # Start recording thread
        
    def stop(self):
        # Stop server - DO NOT USE THIS BEFORE WORLDS HAVE BEEN SAVED
        # If a server binary/executable has an exit command or method - USE THAT FIRST -
        # THIS CAN, (AND THEREFORE SHOULD BE ASSUMED WILL) FORCE CLOSE THE PROCESS 
        self.process.terminate()
        try:
            self.process.wait(timeout=30) # Wait 30 seconds for the program to respond to SIGTERM
        except TimeoutExpired:
            self.process.kill() # Force kill process that took too long to terminate by sending SIGKILL
        finally:
            self.thread.join() # With the process killed and the thread joined, it should have been successfully closed
                               # If this does not work, implement a boolean to _recording_output that will break the for loop


class MinecraftJavaServer(GameServer):
    def __init__(self, version, server_id):
        super().__init__(server_id)
        self.version = version
        # TODO: Add RAM limitations based off what tier the user has chosen to self.args in the form of -Xms and -Xmx
        # 1 is the ID for Minecraft Java Edition
        # Because of the server.properties file, local copies of server.jar are copied into the worlds directory. 
        # This willl make backups easier, especially for reverting back to old versions if an update fails.
        server_dir = get_world_folder(1, self.server_id)
        self.args    = ["java", "-server", "-jar", server_dir + "server.jar", "nogui", "--world", server_dir + "world/"]

    def first_time_setup(self):
        # Check if server.jar for version is installed locally, if not download it
        # Copy server.jar into world directory from local server directory
        # Setup server.properties
        # Agree to Minecraft EULA
        # Start sweet f***ing Minecraft server experience for the customer
        self.start()

    def announce(self, title, subtitle=None):
        """Announce message to all users on server with an alert noise to accompany it."""
        # Play sound with alert
        self.send_input("execute at @a run playsound minecraft:block.note_block.bell ambient @p")
        # Fade in, stay, fade out 
        self.send_input("/title @a time 10 75 5")
        if subtitle:
        # Add subtitle before posting title
            self.send_input('/title @a subtitle {"text":"' + subtitle + '", "color":"white"}')
        self.send_input('/title @a title {"text":"' + title + '", "color":"dark_aqua", "bold":true}')
        

# class MinecraftBedrockServer(GameServer):
#     def __init__(self, args):
#         super().__init__(args)
    
# class DontStarveTogetherServer(GameServer):
#     def __init__(self, args, mods):
#         super().__init__(args)
#         self.mods = mods

# class TerrariaServer(GameServer):
#     def __init__(self, args, version, mods, client):
#         super().__init__(args)
#         self.version = version
#         self.mods = mods
#         if mods:
#             pass
#         else:
#             self.args = ["/opt/terraria/TerrariaServer.bin.x86_64"]
#         self.client = client

# class SCPSLServer(GameServer):

#     def __init__(self):
#         super().__init__()
#         self.mods = None
#         self.args = ["./SCP Secret Laboratory Dedicated Server/LocalAdmin"]
        
