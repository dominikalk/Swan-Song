"""
This file contains variables relating to the player.
"""

from items import *
from map import rooms

inventory = [
    item_key_ceo,
    item_bomb,
    item_key_van,
    item_key_helicopter,
]

# Start game at the lobby
current_room = rooms["trading"]
