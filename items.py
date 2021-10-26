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

item_demo = {
    "id": "demo",
    "name": "the demo",
    "description": """description"""
}


item_bomb = {
    "id": "bomb",
    "name": "the bomb",
    "description": """Bomb description"""
}


items = {
    #   VARIABLE NAME TEMPLATE
    # "<item name>": <VARIABLE OF ITEM>,
    "demo": item_demo,
    "bomb": item_bomb,
}
