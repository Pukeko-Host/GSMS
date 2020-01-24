from gameserver import GameServer
from webserver import ... # Not implemented yet
from json import loads

def json_read(json):
    return loads(json)

def request_servers():
    # Request servers that should be active from motherserver
    pass

def resume_servers():
    if request_servers():
        # Start servers that should be active in this VPS
        pass
    else:
        # No servers should be active in this VPS
        return {}

def main():
    # Define dictionary of gameservers running on this VPS {serverID: GameServer instance}
    gameservers = resume_servers()
    


if __name__ == "__main__":
    main()
