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


items = {
    #   VARIABLE NAME TEMPLATE
    # "<item name>": <VARIABLE OF ITEM>,
    "ceo-key": item_key_ceo,
    "van-key": item_key_van,
    "helicopter-key": item_key_helicopter,
    "bomb": item_bomb,
}
