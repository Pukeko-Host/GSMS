"""
GameServer classes that operate dedicated server executables
Managed by GSMS.py
Requires to be run on POSIX OSes (Tested and designed for Linux VPS machines)
"""

from pty import openpty
from subprocess import Popen, PIPE
from threading import Thread

class GameServer():
    """
    Object for handling server processes in the terminal
    """
    def __init__(self, args):
        self.stdout_output  = []
        self.stdout_handle  = None
        self.stdin_handle   = None
        self.process        = None
        self.args           = args

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
        self.process = Popen(self.args, stdin=PIPE, stdout=slave, close_fds=True, universal_newlines=True)
        self.stdin_handle = self.process.stdin # Use stdin_handle for interactions with the stdin of process
        self.stdout_handle = open(master) # Use stdout_handle for reading the stdout of process

    def _start_recording_thread(self):
        Thread(target=self._record_output, daemon = True).start()

    def start(self):
        # Start server
        self._start_server()
        self._start_recording_thread()


class MinecraftJavaServer(GameServer):
    def __init__(self, args, version, mods, client):
        super().__init__(args)
        self.version = version
        self.mods = mods
        self.client = client

class MinecraftBedrockServer(GameServer):
    def __init__(self, args):
        super().__init__(args)
    
class DontStarveTogetherServer(GameServer):
    def __init__(self, args, mods):
        super().__init__(args)
        self.mods = mods

class TerrariaServer(GameServer):
    def __init__(self, args, version, mods, client):
        super().__init__(args)
        self.version = version
        self.mods = mods
        self.client = client







### For testing

def main():
    path = "/opt/terraria/TerrariaServer.bin.x86_64"
    TerrariaServer = GameServer([path])

    TerrariaServer.start()

    TerrariaServer.send_input("d 1\ny\n")
    
    print(TerrariaServer.stdout_output)

if __name__ == "__main__":
    main()