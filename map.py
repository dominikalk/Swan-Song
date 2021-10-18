'''This file contains a dictionary containing all the rooms in the game.
Structure of a room:

room_<room name> = {
    "name": "<room name long form>",

    "description": """<room description>""",

    "exits": {"<direction>": "<next room>"},

    "items": [<list of ITEM VARIABLES>]
 }
'''

from items import *

room_demo = {
    "name": "demo",

    "description":
    """demo description""",

    "exits": {},

    "items": []
}

rooms = {
    #   VARIABLE NAME TEMPLATE
    # "<room name>": <VARIABLE OF ROOM>,
    "demo": room_demo
}
