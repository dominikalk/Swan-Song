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
    "description": """You enter the middle of the stairwell, in front of you, there are steps leading both up and down. There is also a door leading to security.""",
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
            'time': 5,
        }
    },
}

stairs_basement = {
    "id": "stairs-basement",
    'floor': 'the basement',
    "name": "the stairs",
    "description": """You enter the basement stairs, there is a staircase leading up to the middle floor. To the north, there is the depository, to the east there is the cargo room and to the south there is a server room.""",
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
            'time': 5,
        },
        'east': {
            'room': 'cargo',
            'time': 15,
        },
        'south': {
            'room': 'server',
            'time': 5,
        }
    },
}

stairs_roof = {
    "id": "stairs-roof",
    'floor': 'the roof',
    "name": "the stairs",
    "description": """You enter the stairs, there is a door, through which, you catch a glimpse of the helicopter on the helipad. There are also steps leading down to the middle floor.""",
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
    "description": """Walls filled with small lockable draws that stretch from the floor to the ceiling in the centre of the room lays a table in which they use to sort the items a sorting ladder is attached to each side of the depository to help staff get to the top boxes""",
    "items": [item_watches, item_bonds, item_artifacts, item_jewelry],
    "required_items": [item_depository_keys],
    "locked": True,
    "exits": {
        'north': {
            'room': 'vault',
            'time': 5,
        },
        'east': {
            'room': 'armoury',
            'time': 10,
        },
        'south': {
            'room': 'stairs-basement',
            'time': 5,
        },
    },
}

room_server = {
    "id": "server",
    'floor': 'the basement',
    "name": "the server room of the bank",
    "description": """The room has state of the art network infrastructure, the deafening sound of the cooling infrastructure and the whirring of the hard drives of the server unit. The cables neatly wrap around the server unit casing.""",
    "items": [item_cctv_footage],
    "required_items": [],
    "locked": False,
    "exits": {
        'east': {
            'room': 'electrical',
            'time': 5,
        },
        'north': {
            'room': 'stairs-basement',
            'time': 5,
        },
    },
}

room_armoury = {
    "id": "armoury",
    'floor': 'the basement',
    "name": "the armoury of the bank",
    "description": """You have entered the armoury the steel walls feel cold to the touch the metallic colour glints with the light from the overhead fixtures, the gun racks are locked all but one the body armour is contained on racks within a cabinet.\nThere seems to be a structural abnormality with the one wall it seems to be thinner than the others. A rush of water or a liquid is coming from behind it.""",
    "items": [item_bullet_proof_vest, item_dynamite, item_machine_gun, item_van_keys],
    "required_items": [item_armoury_keys],
    "locked": True,
    "exits": {
        'south': {
            'room': 'cargo',
            'time': 5,
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
    "description": """A large warehouse-like room, the ceiling towers above you with huge shelving units. There are several boxes stacked on the shelves, each of them has stickers relating to their contents. There is also an underground parking for the armoured security vans with a ramp that leads out onto the road above there is a singular van within the cargo bay.""",
    "items": [item_rope, item_bleach, item_10_dollars],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'armoury',
            'time': 5,
        },
        'south': {
            'room': 'electrical',
            'time': 10,
        },
        'west': {
            'room': 'stairs-basement',
            'time': 15,
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
    "description": """You are in the vault a large arched room covered in steel plating armoured bars cover a section at the back of the room that has been left open in there lies a large artifact. Large amounts of cash lay neatly stacked around the room on carts along with gold bullions piled on a central island in the middle of the vault.""",
    "items": [item_1million_dollars, item_gold_bricks],
    "required_items": [],
    "locked": True,
    "exits": {
        'south': {
            'room': 'depository',
            'time': 5,
        },
    },
}

room_electrical = {
    "id": "electrical",
    'floor': 'the basement',
    "name": "the electrical room of the bank",
    "description": """You enter a room full of wires, slithering along and up the wall. The sound of a generator fills the room, providing the only illumination to the room. The control panel hangs on the left.""",
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
            'time': 5,
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
    "description": """A vast open room lays before you large stone pillars tower up to meet the ceiling. The marble floor glistens with the sunlight that cascades through the large bay windows. Crimson blood trickles across the floor towards the door.""",
    "items": [item_newspaper, item_map, item_sculpture],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'tellers',
            'time': 5,
        },
        'east': {
            'room': 'offices',
            'time': 15,
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
    "description": """You face the desk with the large glass shielding that usually separates staff from the public. To the north is security and to the south is the lobby.""",
    "items": [item_10k_dollars, item_crystal],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'security',
            'time': 5,
        },
        'south': {
            'room': 'lobby',
            'time': 5,
        },
    },
}

room_offices = {
    "id": "offices",
    'floor': 'the ground floor',
    "name": "the offices",
    "description": """You enter the offices, the room is large and carries on for seemingly miles there are desk in lines like soldiers in formation. Computers sit on top of them with stacks of files and telephones. The sunshine streams through the blinds of the large office windows.""",
    "items": [item_5k_dollars, item_opal_necklace, item_depository_keys],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'trading',
            'time': 10,
        },
        'south': {
            'room': 'lobby',
            'time': 15,
        },
        'west': {
            'room': 'security',
            'time': 5,
        },
    },
}

room_security = {
    "id": "security",
    'floor': 'the ground floor',
    "name": "the security room",
    "description": """Within the room, the wall is lined with monitors displaying the security feed of the cameras, supplying much of the light in the room. To the north is trading, to east is offices and to the south is the tellers desk.""",
    "items": [item_iphone_13, item_ceo_office_keys, item_armoury_keys],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'trading',
            'time': 5,
        },
        'east': {
            'room': 'offices',
            'time': 5,
        },
        'south': {
            'room': 'tellers',
            'time': 5,
        },
        'west': {
            'room': 'stairs-ground',
            'time': 5,
        },
    },
}

room_trading = {
    "id": "trading",
    'floor': 'the ground floor',
    "name": "the trading room",
    "description": """Usually busy this now desolate room, the large monitors showing the ever evolving stock market laptop lie all over the room on the desks. clipboards of the staff all show the stocks that they are watching that now lay strewn over the floor.""",
    "items": [item_laptop, item_1k_dollars],
    "required_items": [],
    "locked": False,
    "exits": {
        'north': {
            'room': 'ceo',
            'time': 5,
        },
        'east': {
            'room': 'offices',
            'time': 10,
        },
        'south': {
            'room': 'security',
            'time': 5,
        },
    },
}

room_ceo = {
    "id": "ceo",
    'floor': 'the ground floor',
    "name": "the CEO's office",
    "description": """You are in the CEO’s room, a modern sophisticated room with borderless windows that look out onto the city skyline, a large wood and metal table with a leather office chair on the other side with two smaller chairs for clients to sit. A myriad of files strung across the desk, along with a laptop and phone system. The floor seems to bounce quite a bit when you walk; it seems like the floor is really weak.""",
    "items": [item_helicopter_keys, item_100k_dollars, item_golden_watch, item_painting],
    "required_items": [item_ceo_office_keys],
    "locked": True,
    "exits": {
        'south': {
            'room': 'trading',
            'time': 5,
        },
    },
}

# --------- Roof ----------------------

room_helipad = {
    "id": "helipad",
    'floor': 'the roof',
    "name": "the helipad",
    "description": """The roof has a large helipad raised to the rest of the roof. There is a ramp that leads up onto the helipad. An H is painted across it with landing lights dotted at even points around the landing pad and red lights flash intermittently. A modern luxury helicopter is parked on top of it.""",
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
    "required_items": [item_helicopter_keys],
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
      |_____________________| __|__
                 |           |     |
     _____    ___|________   |  O  |
    |     |  |            |  |  F  |
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
