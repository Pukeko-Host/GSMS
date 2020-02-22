"""
Manages GameServer objects by carrying out instructions from Mother Server
Due to requirements of GS.py this must be run on POSIX (Tested and designed for Linux VPS machines)
"""

import GameServer
from webserver import ... # Not implemented yet
from json import loads

def update():
    """Closes GSMS.py, updates library and resume control over servers by using screen"""
    pass

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
        # Load servers from screen that should be active in this VPS
        pass
        # Restart servers that cannot be found, track error
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
