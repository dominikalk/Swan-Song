'''
This script contains variables for all of the items in the game.

Structure of an item:

item_<item name> = {
    "id": "<item id>",

    "name": "<item name>",

    "description": """<item description>"""

    "value": <integer>,

    "time": integer (time taken to interact with the item if it is a special item)
}
'''

item_key_ceo = {
    "id": "ceo-key",
    "name": "the CEO's office key",
    "description": """ceo key description"""
}

item_key_van = {
    "id": "van-key",
    "name": "the armoured van's key",
    "description": """armoured van's key description"""
}

item_key_helicopter = {
    "id": "helicopter-key",
    "name": "the helicopter's key",
    "description": """helicopter's key description"""
}

item_bomb = {
    "id": "bomb",
    "name": "the bomb",
    "description": """Bomb description"""
}

###################room_lobby##########################


item_newspaper = {
    "id": "newspaper",

    "name": "Today's Paper",

    "description": """A large broadsheet newspaper with the breaking headline CEO flies into Manhattan bank this morning. It also has contained information about a transfer that is occurring at some point from the bank. """,

    "value": 3,

    "time": 15


}

item_hostage_car_keys = {
    "id": "hostage car keys",

    "name": "Hostage Car Keys",

    "description": """A set of keys to a car that belong to one of the hostages in the lobby. """,

    "value": 50,

    "time": 10


}



item_map = {
    "id": "map",

    "name": "Map Of The Bank",

    "description": """A detailed map of the bank layout that was in possession of one of the staff members in the lobby. """,

    "value": 30,

    "time": 10 


}



item_sculpture = {
    "id": "sculpture",

    "name": "Henry Moore’s Sculpture",

    "description": """A rare collectable that is worth 1000’s to the right collector, a highly sought-after artifact. """,

    "value": 75000,

    "time": 60

}


###############room_tellers################################



item_10k_dollars = {
    "id": "$10,000",

    "name": "$10,000 Cash",

    "description": """Stacks of cash equalling the approximate sum of 10,000. """,

    "value": 10000,

    "time": 40 


}

item_crystal = {
    "id": "crystal",

    "name": "Crystal Stone",

    "description": """A crystal stone, this valuable gemstone might be worth significant sums to a gem collector or jeweller. """,

    "value": 750,

    "time": 10



}



######################room_cargo#########################



item_rope = {
    "id": "rope",

    "name": "Rope",

    "description": """A long line of climbing grade rope used by the maintenance staff for repairs. """,

    "value": 15,

    "time": 75


}


item_toolbox = {
    "id": "toolbox",

    "name": "Toolbox",

    "description": """A sophisticated toolbox containing a vast range of tools such as a pair of pliers and a screwdriver. """,

    "value": 20,

    "time": 40


}

item_bolt_cutters = {
    "id": "bolt cutters",

    "name": "Bolt Cutters",

    "description": """A set of bolt cutters, with the left handle being slightly rusted, closed with a strong looking clasp. """,

    "value": 7,

    "time": 40


}


item_bleach = {
    "id": "bleach",

    "name": "Bleach",

    "description": """A large bottle of industrial grade bleach with the a sticker on the side the sticker reads ‘OFFICES ONLY’. """,

    "value": 10,

    "time": 30
}


item_10_dollars = {
    "id": "$10",

    "name": "$10 Cash",

    "description": """A single $10 note looks heavily worn but still usable. """,

    "value": 10,

    "time": 3
}




##########room_server###########################




item_cctv_footage = {
    "id": "cctv footage",

    "name": "CCTV Camera Footage",

    "description": """A server unit that contains a sizable amount of CCTV footage that contains evidence of the heist. """,

    "value": 5,

    "time": 5
}


item_electrical_room_key = {
    "id": "electrical room key",

    "name":  "Electrical Room Key",

    "description": """A blue key with a tag on it that reads ‘electrical room’ clearly left behind by the maintenance staff. """,

    "value": 7,

    "time": 5
}


########room_trading########################



item_laptop = {
    "id": "laptop",

    "name": "Laptop",

    "description": """A top of the range laptop used by one of the staff on the trading floor. """,

    "value": 1000,

    "time": 20
}


item_1k_dollars = {
    "id": "$1000",

    "name": "$1000 Cash",

    "description": """A myriad of notes totalling the approximate sum of $1000. """,

    "value": 1000,

    "time": 45  
}



############room_offices#################################



item_depository_keys = {
    "id": "depository keys",

    "name": "Depository keys",

    "description": """A large collection of keys that seem to be for the depository boxes. """,

    "value": 140,

    "time": 50 
}


item_5k_dollars = {
    "id": "$5,000",

    "name": "$5,000 Cash",

    "description": """A pile of cash that seemed to be prepared to be moved into the vault. """,

    "value": 5000,

    "time": 75
}


item_opal_necklace = {
    "id": "opal necklace",

    "name": "Opal necklace",

    "description": """A golden chain that holds a rare, large, black opal stone as it’s centre piece. """,

    "value": 1750,

    "time": 15
}


##########room_ceo#######################



item_security_id_card = {
    "id": "security id card",

    "name": "Security ID Card",

    "description": """A security card with the CEO’s name and photo on it with the words ‘security clearance LEVEL 5’. """,

    "value": 10,

    "time": 5
}


item_helicopter_key = {
    "id": "helicopter key",

    "name": "Helicopter Key",

    "description": """A strange pair of keys that appear to be for some sort of aircraft they are contained within a leather pouch. """,

    "value": 7,

    "time": 5
}


item_100k_dollars = {
    "id": "$100,000",

    "name": "$100,000 Cash",

    "description": """A huge sum of cash that appears to all belong to the CEO. """,

    "value": 100,000,

    "time": 90
}


item_golden_watch = {
    "id": "golden watch",

    "name": "Golden Watch",

    "description": """A golden watch with diamond encrusted into the rim of the watch face. """,

    "value": 1995,

    "time": 15
}


item_painting = {
    "id": "painting",

    "name": "Pablo Picasso's Painting",

    "description": """A large complex painting with the artists mark of Picasso inscribed in the right hand corner of the painting. """,

    "value": 250000,

    "time": 55
}



####################room_security#########################




item_armoury_key = {
    "id": "armoury key",

    "name": "Armoury Key",

    "description": """A large key with some text on it that reads ‘armoury’. """,

    "value": 7,

    "time": 5 
}


item_ceo_office_keys = {
    "id": "ceo office keys",

    "name":  "CEO's Office Keys",

    "description": """A set of keys that look to be used by the CEO for their office. """,

    "value": 10,

    "time": 5
}


item_iphone_13 = {
    "id": "iphone 13",

    "name": "iPhone 13 pro max",

    "description": """A state of the art flagship phone used by the CEO, it has a picture of a dog on the lock screen. """,

    "value": 1075,

    "time": 15
}

#######################room_armoury###################

item_bullet_proof_vest = {
    "id": "bullet proof vest",

    "name": "Bullet Proof Vest",

    "description": """A large ballistic vest composed of Kevlar and metal plates, it is of military grade used by the guards for protection. """,

    "value": 350,

    "time": 20 
}



item_dynamite = {
    "id": "dynamite",

    "name": "Dynamite",

    "description": """Several sticks of dynamite with a letter attached to it stating it is for transfer. """,

    "value": 20000,

    "time": 30 
}


item_machine_gun = {
    "id": "machine gun",

    "name": "Machine Gun",

    "description": """S military grade mp5 with a holographic sight with sling. """,

    "value": 85000,

    "time": 30
}


item_jackhammer = {
    "id": "jackhammer",

    "name": "Jackhammer",

    "description": """A industrial grade jackhammer used in the construction industry to mine out vast quantities of rock and concrete. """,

    "value": 1600,

    "time": 70
}

item_cutting_torch = {
    "id": "cutting torch",

    "name": "Cutting Torch",

    "description": """A plasma cutting torch used to effortlessly cut through metal for building purposes. """,

    "value": 230,

    "time": 30
}



######################room_electrical####################


item_electrical_generator = {
    "id": "electrical generator",

    "name": "Electrical Generator",

    "description": """A sophisticated power grid with an auxiliary backup the generator has a control panel attached to it that controls the building power network. """,

    "value": 1000,

    "time": 5
}


#####################room_vault#############################




item_1000k_dollars = {
    "id": "$1,000,000",

    "name": "$1,000,000 Cash",

    "description": """Vast stack of cash all stacked all in bags ready for the transport. """,

    "value": 1000000,

    "time": 120 
}

item_gold_bricks = {
    "id": "gold bricks",

    "name": "Gold Bricks",

    "description": """Stacks of gold bullions all of them have different ID numbers engraved into them. """,

    "value": 1000000,

    "time": 240
}



######################room_depository###################



item_watches = {
    "id": "watches",

    "name": "Watches",

    "description": """A collection of highly valuable watches that would of significant value. """,

    "value": 35000,

    "time": 100
}


item_bonds = {
    "id": "bonds",

    "name":  "Bonds",

    "description": """A large volume of bonds worth a lot of money to investors. """,

    "value": 45000,

    "time": 60
}


item_artifacts = {
    "id": "artifacts",

    "name": "Artifacts",

    "description": """Rare artifacts of historic significant value is unknown. """,

    "value": 55000,

    "time": 180
}


item_jewelry = {
    "id": "jewelry",

    "name": "Jewelry",

    "description": """Significant volumes of jewelry likely belonging to wealthy bank clients that wanted it stored away. """,

    "value": 42500,

    "time": 150
}







items = {
    #   VARIABLE NAME TEMPLATE
    # "<item name>": <VARIABLE OF ITEM>,
    "ceo-key": item_key_ceo,
    "van-key": item_key_van,
    "helicopter-key": item_key_helicopter,
    "bomb": item_bomb,
    "newspaper": item_newspaper,
    "hostage car keys": item_hostage_car_keys,
    "map": item_map,
    "sculpture": item_sculpture,
    "$10,000": item_10k_dollars,
    "crystal": item_crystal,
    "rope": item_rope,
    "toolbox": item_toolbox,
    "bolt cutters": item_bolt_cutters,
    "bleach": item_bleach,
    "$10": item_10_dollars,
    "cctv footage": item_cctv_footage,
    "electrical room key": item_electrical_room_key,
    "laptop": item_laptop,
    "$1000": item_1k_dollars,
    "depository keys": item_depository_keys,
    "$5,000": item_5k_dollars,
    "opal necklace": item_opal_necklace,
    "security id card": item_security_id_card,
    "helicopter key": item_helicopter_key,
    "$100,000": item_100k_dollars,
    "golden watch": item_golden_watch,
    "painting": item_painting,
    "armoury key": item_armoury_key,
    "ceo office keys": item_ceo_office_keys,
    "iphone 13": item_iphone_13,
    "bullet proof vest": item_bullet_proof_vest,
    "dynamite": item_dynamite,
    "machine gun": item_machine_gun,
    "jackhammer": item_jackhammer,
    "cutting torch": item_cutting_torch,
    "electrical generator": item_electrical_generator,
    "$1,000,000": item_1000k_dollars,
    "gold bricks": item_gold_bricks,
    "watches": item_watches,
    "bonds": item_bonds,
    "artifacts": item_artifacts,
    "jewelry": item_jewelry




}
