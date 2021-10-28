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
    "items": [item_watches, item_bonds, item_artifacts, item_jewelry],
    "required_items": [item_depository_keys],
    "locked": True,
    "exits": {
        'north': {
            'room': 'vault',
            'time': 10,
        },
        'east': {
            'room': 'armoury',
            'time': 10,
        },
        'south': {
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
    "items": [item_cctv_footage],
    "required_items": [],
    "locked": False,
    "exits": {
        'east': {
            'room': 'electrical',
            'time': 10,
        },
        'north': {
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
    "items": [item_bullet_proof_vest, item_dynamite, item_machine_gun, item_jackhammer, item_cutting_torch],
    "required_items": [item_armoury_key],
    "locked": True,
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
    "items": [item_rope, item_toolbox, item_bolt_cutters, item_bleach, item_10_dollars],
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
    "required_items": [item_van_keys],
    "locked": True,
    "exits": {}
}

room_vault = {
    "id": "vault",
    'floor': 'the basement',
    "name": "the vault of the bank",
    "description": """The vault description""",
    "items": [item_1million_dollars, item_gold_bricks],
    "required_items": [],
    "locked": True,
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
    "items": [item_electrical_generator],
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
    "items": [item_newspaper, item_van_keys, item_map, item_sculpture],
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
    "items": [item_10k_dollars, item_crystal],
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
    "items": [item_5k_dollars, item_opal_necklace],
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
    "items": [item_iphone_13, item_ceo_office_keys, item_armoury_key],
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
    "items": [item_laptop, item_1k_dollars],
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
    "items": [item_helicopter_key, item_100k_dollars, item_golden_watch, item_painting],
    "required_items": [item_ceo_office_keys],
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
    "required_items": [item_helicopter_key],
    "locked": True,
    "exits": {}
}

rooms = {
    # Stairs
    'stairs-basement': stairs_basement,
    'stairs-ground': stairs_ground,
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
             THE ROOF 
             --------
                 ___________            
     _____      |           |
    |     |     |           |
    |  S  |_____|  HELIPAD  |
    |_____|     |           |
                |___________|
    
           -----------
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
            THE BASEMENT
            ------------
     ___________       _________
    |   VAULT   |     |         |
    |___________|   __| ARMOURY |
    |           |__|  |_________|
    | DEPOSITORY|  ________|____
    |___________| |             |
     __|__     ___|    CARGO    |
    |     |   |   |_____________|
    |  S  |___|            |
    |_____|                |
     __|_____     _________|____   
    |        |   |              |
    | SERVER |___|  ELECTRICAL  |
    |________|   |______________|
    
            ----------
            STAIRS = S
'''
}
