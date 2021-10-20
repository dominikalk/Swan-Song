'''This file contains a dictionary containing all the rooms in the game.
Structure of a room:

room_<room name> = {
    "id": "<room name short form>"

    "name": "<room name long form>",

    "description": """<room description>""",

    "items": [<list of ITEM VARIABLES>]

    "exits": {
        "<direction>" = {
            "room": "<next room>",
            "time": "<time used to move>",
            "locked": <boolean>  (default to false)
        }
    },
 }
'''

from items import *

room_demo = {
    "name": "demo",

    "description": """demo description""",
    
    "items": [],

    "exits": {},
}

rooms = {
    #   VARIABLE NAME TEMPLATE
    # "<room name>": <VARIABLE OF ROOM>,
    "demo": room_demo
}
