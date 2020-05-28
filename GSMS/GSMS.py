"""
Manages GameServer objects by carrying out instructions from Mother Server
Due to requirements of GS.py this must be run on POSIX (Designed for a Linux VPS, developed on Manjaro Linux 20 and tested on Debian 10)
"""

import GS as GameServer
# from webserver import ... Not implemented yet
from json import loads

def update():
    """Closes GSMS.py, updates library and resume control over servers by using screen"""
    pass

def json_read(json):
    return loads(json)

def recieve_request():
    json = None
    if (read_json := json_read(json)):
        
        read_json['serverId']
        read_json['gameserverId']
        read_json['game']
        read_json['command']

def request_servers():
    # Request servers that should be active from motherserver
    # Recieve JSON object
    return None

def resume_servers():
    if request_servers():
        # Load servers from screen that should be active in this VPS
        pass
        # Restart servers that cannot be found, track error
    else:
        # No servers should be active in this VPS
        return {}

def start_server(user_id, game_id, gameservers):
    # GameServers in an array where their index is their game_id - 1, alternative being a dict with keys from 1 to n. 
    # In my opinion this option is preferable.
    server = [
        GameServer.MinecraftJavaServer,
        GameServer.MinecraftBedrockServer,
        GameServer.DontStarveTogetherServer,
        GameServer.TerrariaServer,
        GameServer.SCPSLServer
    ][game_id - 1]()

    print(server) # for debugging

    if len(gameservers):
        gameserver_id = gameservers.keys()[-1] + 1
    else:
        gameserver_id = 0

    gameservers[gameserver_id] = server
    server.start()

    return gameserver_id

def stop_server(gameserver_id, gameservers):
    gameservers[gameserver_id].stop()
    del gameservers[gameserver_id]

def main():
    # Define dictionary of gameservers running on this VPS {serverID: GameServer instance}
    gameservers = resume_servers()
    # Start Async background task for listening to Mother - Not implemented yet -
    return gameservers
    
