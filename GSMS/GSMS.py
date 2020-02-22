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
