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

The structure for stairs is similar except the exit names also include 'up' 
and 'down' and the variable name is prefaced with 'stairs'
'''

from items import *

# --------- Stairs ----------------------

stairs_ground = {
    "id": "stairs-ground",
    "name": "the ground floor stairs",
    "description": """The ground floor stairs description""",
    "items": [],
    "exits": {
        'up': {
            'room': 'stairs-roof',
            'time': 0,
            'locked': False
        },
        'down': {
            'room': 'stairs-basement',
            'time': 0,
            'locked': False
        },
        'east': {
            'room': 'security',
            'time': 0,
            'locked': False
        }
    },
}

stairs_basement = {
    "id": "stairs-basement",
    "name": "the basement floor stairs",
    "description": """The basement floor stairs description""",
    "items": [],
    "exits": {
        'up': {
            'room': 'stairs-ground',
            'time': 0,
            'locked': False
        },
        'east': {
            'room': 'cargo',
            'time': 0,
            'locked': False
        },
        'north': {
            'room': 'depository',
            'time': 0,
            'locked': False
        },
        'south': {
            'room': 'server',
            'time': 0,
            'locked': False
        }
    },
}

stairs_roof = {
    "id": "stairs-roof",
    "name": "the roof stairs",
    "description": """The roof stairs description""",
    "items": [],
    "exits": {
        'down': {
            'room': 'stairs-ground',
            'time': 0,
            'locked': False
        },
        'east': {
            'room': 'roof',
            'time': 0,
            'locked': False
        },
    },
}

# --------- Basement ----------------------

room_depository = {
    "id": "depository",
    "name": "the depository of the bank",
    "description": """The depository description""",
    "items": [],
    "exits": {
        'west': {
            'room': 'stairs-basement',
            'time': 0,
            'locked': False
        },
        'east': {
            'room': 'armoury',
            'time': 0,
            'locked': False
        },
        'north': {
            'room': 'vault',
            'time': 0,
            'locked': False
        }
    },
}

room_server = {
    "id": "server",
    "name": "the server room of the bank",
    "description": """The server room description""",
    "items": [],
    "exits": {
        'west': {
            'room': 'stairs-basement',
            'time': 0,
            'locked': False
        },
        'east': {
            'room': 'electrical',
            'time': 0,
            'locked': False
        }
    },
}

room_armoury = {
    "id": "armoury",
    "name": "the armoury of the bank",
    "description": """The armoury description""",
    "items": [],
    "exits": {
        'west': {
            'room': 'depository',
            'time': 0,
            'locked': False
        },
        'south': {
            'room': 'cargo',
            'time': 0,
            'locked': False
        }
    },
}

room_cargo = {
    "id": "cargo",
    "name": "the cargo loading bay of the bank",
    "description": """The cargo loading bay description""",
    "items": [],
    "exits": {
        'west': {
            'room': 'stairs-basement',
            'time': 0,
            'locked': False
        },
        'south': {
            'room': 'electrical',
            'time': 0,
            'locked': False
        },
        'north': {
            'room': 'armoury',
            'time': 0,
            'locked': False
        },
    },
}

room_vault = {
    "id": "vault",
    "name": "the vault of the bank",
    "description": """The vault description""",
    "items": [],
    "exits": {
        'south': {
            'room': 'depository',
            'time': 0,
            'locked': False
        },
    },
}

room_electrical = {
    "id": "electrical",
    "name": "the electrical room of the bank",
    "description": """The electrical room description""",
    "items": [],
    "exits": {
        'west': {
            'room': 'server',
            'time': 0,
            'locked': False
        },
        'north': {
            'room': 'cargo',
            'time': 0,
            'locked': False
        }
    },
}

# --------- Ground Floor ----------------------

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
    "description": """The tellers description""",
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
    "description": """The offices description""",
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
    "description": """The security description""",
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
            'room': 'stairs-ground',
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
    "description": """The ceo's office description""",
    "items": [],
    "exits": {
        'south': {
            'room': 'trading',
            'time': 0,
            'locked': False
        },
    },
}

# --------- Roof ----------------------

room_roof = {
    "id": "roof",
    "name": "the roof",
    "description": """The roof description""",
    "items": [],
    "exits": {
        'west': {
            'room': 'stairs-roof',
            'time': 0,
            'locked': False
        },
    },
}

rooms = {
    # Stairs
    'stairs-ground': stairs_ground,
    'stairs-basement': stairs_basement,
    'stairs-roof': stairs_roof,

    # Basement
    'server': room_server,
    'electrical': room_electrical,
    'cargo': room_cargo,
    'armoury': room_armoury,
    'depository': room_depository,
    'vault': room_vault,

    # Ground Floor
    'lobby': room_lobby,
    'tellers': room_tellers,
    'office': room_office,
    'security': room_security,
    'ceo': room_ceo,

    # Roof
    'roof': room_roof
}
