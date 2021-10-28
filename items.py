'''
This script contains variables for all of the items in the game.

Structure of an item:

item_<item name> = {
    "id": "<item id>",

    "name": "<item name>",

    "description": """<item description>"""

    "value": <integer>,
}
'''

item_key_ceo = {
    "id": "ceo-key",
    "name": "the CEO's office key",
    "description": """ceo key description""",
    "value": 5,
}

item_key_van = {
    "id": "van-key",
    "name": "the armoured van's key",
    "description": """armoured van's key description""",
    "value": 5,
}

item_key_helicopter = {
    "id": "helicopter-key",
    "name": "the helicopter's key",
    "description": """helicopter's key description""",
    "value": 5,
}

item_bomb = {
    "id": "bomb",
    "name": "the bomb",
    "description": """Bomb description""",
    "value": 1000,
}

item_rope = {
    "id": "rope",
    "name": "Rope",
    "description": """A long line of climbing grade rope used by the maintenance staff for repairs. """,
    "value": 5,
}


items = {
    #   VARIABLE NAME TEMPLATE
    # "<item name>": <VARIABLE OF ITEM>,
    "ceo-key": item_key_ceo,
    "van-key": item_key_van,
    "helicopter-key": item_key_helicopter,
    "bomb": item_bomb,
    "rope": item_rope,
}
