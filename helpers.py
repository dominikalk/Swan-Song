"""
This helpers folder will contain a lot of the subroutines that we dont want in other files
as it would clutter them. We might make more helper files if this one gets too large.
"""

from map import rooms, map_design


def capitalise_sentence(string):
    string_list = string.split()
    string = ""
    for i, x in enumerate(string_list):
        if x.upper() != x:
            x = x[0].upper() + x[1:]
        if i == len(string_list) - 1:
            string += x
        else:
            string += x + " "
    return string


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:
    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'
    >>> list_of_items([item_id])
    'id card'
    >>> list_of_items([])
    ''
    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'
    """

    list_of_items = []
    for i in items:
        items = i["name"]
        list_of_items.append(str(items))
        item_num = len(list_of_items)
    if item_num > 2:
        list_of_items.insert(-1, ' and') 
        items = ', '.join(list_of_items[:-2]) + ' '.join(list_of_items[-2:])
        return items 
    elif item_num == 2:
        items = " and ".join(list_of_items)
        return items
    else:
        return items


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:
    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>
    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>
    >>> print_room_items(rooms["Admins"])
    (no output)
    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """

    if(len(room['items']) == 0):
        return

    print(f'There is {list_of_items(room["items"])} here.\n')


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:
    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>
    """

    if(len(items) == 0):
        return

    print(f'You have {list_of_items(items)}.\n')


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:
    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>
    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>
    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>
    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(capitalise_sentence(room["floor"]))
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()

    # Display items in the room
    print_room_items(room)


def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:
    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """

    return rooms[exits[direction]["room"]]['name']


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:
    GO <EXIT NAME UPPERCASE> to <where it leads>.
    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print
    "TAKE <ITEM ID> to take <item name>."
    and for each item in the inventory print
    "DROP <ITEM ID> to drop <item name>."
    For example, the menu of actions available at the Reception may look like this:
    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?
    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    # Iterate over available take actions
    for item in room_items:
        # Print the exit name and where it leads to
        print(f'TAKE {item["id"].upper()} to take {item["name"]}.')

    # Iterate over available take actions
    for item in inv_items:
        # Print the exit name and where it leads to
        print(f'DROP {item["id"].upper()} to drop {item["name"]}.')

    print("What do you want to do?\n")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:
    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:
    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]['room']]


def format_time(time):
    minutes = int(time // 60)
    seconds = int(time % 60)
    time = f'{minutes:02}:{seconds:02}'
    return time


def format_price(value):
    numstring = str(value)
    stringplace = 0
    final_string = ""

    for char in numstring[::-1]:
        stringplace = stringplace + 1
        final_string = char + final_string
        if stringplace % 3 == 0 and stringplace != 0:
            if stringplace != len(numstring):
                final_string = "," + final_string
    final_string = "$" + final_string
    return final_string


def print_time(time_used, time_left):
    time_used_formatted = format_time(time_used)
    time_left_formatted = format_time(time_left)
    print(f"You have been in the heist for {time_used_formatted} seconds.")
    print(f"You have {time_left_formatted} seconds until SWAT storm the bank.")


def calculate_value(item_list):
    total_value = 0
    for item in item_list:
        item_value = item["value"]
        total_value = total_value + int(item_value)
    return total_value


def display_map(current_room):
    floor = current_room['floor']
    print(map_design[floor])
