'''This file contains a dictionary containing all the rooms in the game.
Structure of a room:

room_<room name> = {
    "id": "<room name short form>"

    "floor": "<floor name>",

    "name": "<room name long form>",

    "description": """<room description>""",

    "items": [<list of ITEM VARIABLES>],

    "required_items": [<list of ITEM VARIABLES>], (items needed to unlock or access a room)

    "locked": <boolean>  (default to false)

    "exits": {
        "<direction>" = {
            "room": "<next room>",
            "time": "<time used to move>",
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
    'floor': 'the ground floor',
    "name": "the stairs",
    "description": """The ground floor stairs description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'up': {
            'room': 'stairs-roof',
            'time': 10,
        },
        'down': {
            'room': 'stairs-basement',
            'time': 10,
        },
        'east': {
            'room': 'security',
            'time': 10,
        }
    },
}

stairs_basement = {
    "id": "stairs-basement",
    'floor': 'the basement',
    "name": "the stairs",
    "description": """The basement floor stairs description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'up': {
            'room': 'stairs-ground',
            'time': 10,
        },
        'north': {
            'room': 'depository',
            'time': 10,
        },
        'east': {
            'room': 'cargo',
            'time': 10,
        },
        'south': {
            'room': 'server',
            'time': 10,
        }
    },
}

stairs_roof = {
    "id": "stairs-roof",
    'floor': 'the roof',
    "name": "the stairs",
    "description": """The roof stairs description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'down': {
            'room': 'stairs-ground',
            'time': 10,
        },
        'east': {
            'room': 'helipad',
            'time': 10,
        },
    },
}

# --------- Basement ----------------------

room_depository = {
    "id": "depository",
    'floor': 'the basement',
    "name": "the depository of the bank",
    "description": """The depository description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'vault',
            'time': 10,
        },
        'east': {
            'room': 'armoury',
            'time': 10,
        },
        'west': {
            'room': 'stairs-basement',
            'time': 10,
        },
    },
}

room_server = {
    "id": "server",
    'floor': 'the basement',
    "name": "the server room of the bank",
    "description": """The server room description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'east': {
            'room': 'electrical',
            'time': 10,
        },
        'west': {
            'room': 'stairs-basement',
            'time': 10,
        },
    },
}

room_armoury = {
    "id": "armoury",
    'floor': 'the basement',
    "name": "the armoury of the bank",
    "description": """The armoury description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'south': {
            'room': 'cargo',
            'time': 10,
        },
        'west': {
            'room': 'depository',
            'time': 10,
        },
    },
}

room_cargo = {
    "id": "cargo",
    'floor': 'the basement',
    "name": "the cargo loading bay of the bank",
    "description": """The cargo loading bay description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'armoury',
            'time': 10,
        },
        'south': {
            'room': 'electrical',
            'time': 10,
        },
        'west': {
            'room': 'stairs-basement',
            'time': 10,
        },
        'van': {
            'room': 'van',
            'time': 0,
        },
    },
}

# Exit: Vehicle
exit_van = {
    "id": "van",
    'floor': 'the basement',
    "name": "the armoured van",
    "description": """The armoured van description""",
    "items": [],
    "required_items": [item_key_van],
    "locked": True,
    "exits": {}
}

room_vault = {
    "id": "vault",
    'floor': 'the basement',
    "name": "the vault of the bank",
    "description": """The vault description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'south': {
            'room': 'depository',
            'time': 10,
        },
    },
}

room_electrical = {
    "id": "electrical",
    'floor': 'the basement',
    "name": "the electrical room of the bank",
    "description": """The electrical room description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'cargo',
            'time': 10,
        },
        'west': {
            'room': 'server',
            'time': 10,
        },
    },
}

# Secret Room
exit_sewage = {
    "id": "sewage",
    'floor': 'the basement',
    "name": "the sewage tunnel",
    "description": """Sewage tunnel description and escape outro""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {},
}

# --------- Ground Floor ----------------------

exit_front = {
    "id": "exit",
    'floor': 'the ground floor',
    "name": "the front exit",
    "description": """The front exit description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {},
}

room_lobby = {
    "id": "lobby",
    'floor': 'the ground floor',
    "name": "the lobby of the bank",
    "description": """The lobby description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'tellers',
            'time': 10,
        },
        'east': {
            'room': 'offices',
            'time': 10,
        },
        'south': {
            'room': 'exit',
            'time': 0,
        },
    },
}

room_tellers = {
    "id": "tellers",
    'floor': 'the ground floor',
    "name": "the tellers of the bank",
    "description": """The tellers description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'security',
            'time': 10,
        },
        'south': {
            'room': 'lobby',
            'time': 10,
        },
    },
}

room_offices = {
    "id": "offices",
    'floor': 'the ground floor',
    "name": "the offices",
    "description": """The offices description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'trading',
            'time': 10,
        },
        'south': {
            'room': 'lobby',
            'time': 10,
        },
        'west': {
            'room': 'security',
            'time': 10,
        },
    },
}

room_security = {
    "id": "security",
    'floor': 'the ground floor',
    "name": "the security room",
    "description": """The security description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'trading',
            'time': 10,
        },
        'east': {
            'room': 'offices',
            'time': 10,
        },
        'south': {
            'room': 'tellers',
            'time': 10,
        },
        'west': {
            'room': 'stairs-ground',
            'time': 10,
        },
    },
}

room_trading = {
    "id": "trading",
    'floor': 'the ground floor',
    "name": "the trading room",
    "description": """The trading room description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'ceo',
            'time': 10,
        },
        'east': {
            'room': 'offices',
            'time': 10,
        },
        'south': {
            'room': 'security',
            'time': 10,
        },
    },
}

room_ceo = {
    "id": "ceo",
    'floor': 'the ground floor',
    "name": "the CEO's office",
    "description": """The CEO's office description""",
    "items": [],
    "required_items": [item_key_ceo],
    "locked": True,
    "exits": {
        'south': {
            'room': 'trading',
            'time': 10,
        },
    },
}

# --------- Roof ----------------------

room_helipad = {
    "id": "helipad",
    'floor': 'the roof',
    "name": "the helipad",
    "description": """The helipad description""",
    "items": [],
    "required_items": [],
    "locked": False,
    "exits": {
        'west': {
            'room': 'stairs-roof',
            'time': 10,
        },
        'helicopter': {
            'room': 'helicopter',
            'time': 0,
        }
    },
}

# Exit: Vehicle
exit_helicopter = {
    "id": "helicopter",
    'floor': 'the roof',
    "name": "the helicopter",
    "description": """The helicopter description""",
    "items": [],
    "required_items": [item_key_helicopter],
    "locked": True,
    "exits": {}
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
    # Exit: Secret Room, Vehicle
    'sewage': exit_sewage,
    'van': exit_van,

    # Ground Floor
    'lobby': room_lobby,
    'tellers': room_tellers,
    'offices': room_offices,
    'security': room_security,
    'ceo': room_ceo,
    'trading': room_trading,
    # Exit
    'exit': exit_front,

    # Roof
    'helipad': room_helipad,
    # Exit: Vehicle
    'helicopter': exit_helicopter
}


map_design = {
    'the roof':
    '''
ROOF


     
             __________             
            |          |
 _____      |          |
|     |     |          |
|  S  |_____| HELIPAD  |
|_____|     |          |
            |          |
            |__________|

            
STAIRS  = S
''',
    'the ground floor':
    '''
         THE GROUND FLOOR
         ----------------
            _________    
           |         | 
           |   CEO   |
           |_________|
                |     
      __________|__________
     |                     |
     |       TRADING       |___ 
     |_____________________|   |
                |            __|__
    _____    ___|________   |     |
   |     |  |            |  |  O  |
   |  S  |__|  SECURITY  |__|  F  |
   |_____|  |____________|  |  I  |
                  |         |  C  |   
              ____|_____    |  E  |   
             | TELLERS  |   |  S  |   
             |__________|   |_____|   
                  |            |_____
    ______        |         ______   |  
   |      |_______|________|      |  |
   |                              |__|
   |            LOBBY             |
   |______________________________|
                  |
              FRONT EXIT
            --------------
            STAIRS   =   S
''',
    'the basement':
    '''
BASEMENT

             ___________ 
            |   VAULT   | 
            |___________|  __________
            |           |_| ARMOURY  |
        ____| DEPOSITORY| |__________|
       |    |           |      |
     __|__  |___________|    __|____
    |     |                 |       |
    |  S  |_________________| CARGO |
    |_____|                 |       |
       |                    |_______|
       |                        |
       |  ______   __________   |
       | |      | |          |  |
       |_|SERVER|_|ELECTRICAL|__|
         |______| |__________|

STAIRS = S

'''
}
