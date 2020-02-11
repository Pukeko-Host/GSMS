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
