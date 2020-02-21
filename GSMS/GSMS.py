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

import GameServer
from webserver import ... # Not implemented yet
from json import loads

def json_read(json):
    return loads(json)

def recieve_request():
    if (json := json_read()):
        
        json['serverId']
        json['gameserverId']
        json['game']
        json['command']

def request_servers():
    # Request servers that should be active from motherserver
    # Recieve JSON object
    pass



def resume_servers():
    if request_servers():
        # Start servers that should be active in this VPS
        pass
    else:
        # No servers should be active in this VPS
        return {}

def close_server():
    pass

def main():
    # Define dictionary of gameservers running on this VPS {serverID: GameServer instance}
    gameservers = resume_servers()
    


if __name__ == "__main__":
    main()
