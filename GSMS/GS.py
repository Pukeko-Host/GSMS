"""
License Zero Noncommercial Public License 2.0.1

Copyright: Pukeko-Host

Source: 

**This software comes as is, without any warranty at all. As far
as the law allows, I will not be liable for any damages related
to this software or this license, for any kind of legal claim.**

As long as you meet the conditions below, you may do everything
with this software that would otherwise infringe my copyright in
it or any covered patent claim. Your permission covers a patent
claim that I can license, or become able to license, if you would
infringe it by using this software as of my latest contribution.

1. You must ensure that everyone who gets a copy of this software
   from you, in source code or any other form, also gets the
   complete text of this license and the copyright and source
   notices above.

2. You must not make any legal claim against anyone for
   infringing any patent claim they would infringe by using this
   software alone, accusing this software, with or without
   changes, alone or combined into a larger program.

3. You must limit use of this software in any manner primarily
   intended for or directed toward commercial advantage or
   private monetary compensation to a period of 32
   consecutive calendar days. This limit does not apply to use in
   developing feedback, modifications, or extensions that you
   contribute back to those giving this license.
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