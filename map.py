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

room_lobby = {
    "id": "lobby",

    "name": "the lobby of the bank",

    "description": """The lobby description""",
    
    "items": [item_demo],

    "exits": {
        'north': {
            'room': 'tellers',
            'time': 0,
            'locked': False
        },
        'east': {
            'room': 'office',
            'time': 0,
            'locked': False
        } 
    },
}

room_tellers = {
    "id": "tellers",

    "name": "the tellers of the bank",

    "description": """""",
    
    "items": [],

    "exits": {
        'south': {
            'room': 'lobby',
            'time': 0,
            'locked': False
        },
        'north': {
            'room': 'security',
            'time': 0,
            'locked': False
        } 
    },
}

room_office = {
    "id": "office",

    "name": "the offices",

    "description": """""",
    
    "items": [],

    "exits": {
        'south': {
            'room': 'lobby',
            'time': 0,
            'locked': False
        },
        'west': {
            'room': 'security',
            'time': 0,
            'locked': False
        },
        'north': {
            'room': 'trading',
            'time': 0,
            'locked': False
        }
    },
}

room_security = {
    "id": "security",

    "name": "the security room",

    "description": """""",
    
    "items": [],

    "exits": {
        'east': {
            'room': 'office',
            'time': 0,
            'locked': False
        },
        'south': {
            'room': 'tellers',
            'time': 0,
            'locked': False
        },
        'west': {
            'room': 'stairs',
            'time': 0,
            'locked': False
        },
        'north': {
            'room': 'trading',
            'time': 0,
            'locked': False
        }
    },
}

room_ceo = {
    "id": "ceo",

    "name": "the CEO's office",

    "description": """""",
    
    "items": [],

    "exits": {
        'south': {
            'room': 'trading',
            'time': 0,
            'locked': False
        },
    },
}

rooms = {
    #   VARIABLE NAME TEMPLATE
    # "<room name>": <VARIABLE OF ROOM>,
    "lobby": room_lobby,
    'tellers': room_tellers,
    'office': room_office,
    'security': room_security,
    'ceo': room_ceo
}
