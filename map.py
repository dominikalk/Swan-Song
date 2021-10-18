from items import *

#   ROOM TEMPLATE
#   room name in the form room_<room name>
# room_<room name> = {
#     "name": "<room name long form>",

#     "description":
#     """<room description>""",

#     "exits": {"<direction>": "<next room>"},

#     "items": [<list of ITEM VARIABLES>]
# }

room_demo = {
    "name": "demo",

    "description":
    """demo description""",

    "exits": {},

    "items": []
}

rooms = {
    #   VARIABLE NAME TEMPLATE
    # "<room name>": <VARIABLE OF ROOM>,
    "demo": room_demo
}
