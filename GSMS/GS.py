"""
The Prosperity Public License 3.0.0
Contributor: Pukeko-Host

Source Code: https://github.com/Pukeko-Host/GSMS

Purpose
This license allows you to use and share this software for noncommercial purposes for free and
to try this software for commercial purposes for thirty days.

Agreement
In order to receive this license, you have to agree to its rules. Those rules are both obligations 
under that agreement and conditions to your license. Don't do anything with this software that 
triggers a rule you can't or won't follow.

Notices
Make sure everyone who gets a copy of any part of this software from you, with or without 
changes, also gets the text of this license and the contributor and source code lines above.

Commercial Trial
Limit your use of this software for commercial purposes to a thirty-day trial period. If you use this 
software for work, your company gets one trial period for all personnel, not one trial per person.

Contributions Back
Developing feedback, changes, or additions that you contribute back to the contributor on the 
terms of a standardized public software license such as the Blue Oak Model License 1.0.0, the 
Apache License 2.0, the MIT license, or the two-clause BSD license doesn't count as use for a 
commercial purpose.

Personal Uses
Personal use for research, experiment, and testing for the benefit of public knowledge, personal 
study, private entertainment, hobby projects, amateur pursuits, or religious observance, without 
any anticipated commercial application, doesn't count as use for a commercial purpose.

Noncommercial Organizations
Use by any charitable organization, educational institution, public research organization, public 
safety or health organization, environmental protection organization, or government institution 
doesn't count as use for a commercial purpose regardless of the source of funding or obligations 
resulting from the funding.

Defense
Don't make any legal claim against anyone accusing this software, with or without changes, 
alone or with other technology, of infringing any patent.

Copyright
The contributor licenses you to do everything with this software that would otherwise infringe 
their copyright in it.

Patent
The contributor licenses you to do everything with this software that would otherwise infringe 
any patents they can license or become able to license.

Reliability
The contributor can't revoke this license.

Excuse
You're excused for unknowingly breaking Notices if you take all practical steps to comply within 
thirty days of learning you broke the rule.

No Liability
As far as the law allows, this software comes as is, without any warranty or condition, 
and the contributor won't be liable to anyone for any damages related to this software or 
this license, under any kind of legal claim.
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