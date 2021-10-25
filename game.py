#!/usr/bin/python3

"""
This file contains the main game loop.
"""

from player import *
from items import *
from gameparser import *
from helpers import *

# Time is measured in seconds
time_used = 0
time_left = 1800  # 30 minutes but overall time available may change due to negotiations


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.
    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    global current_room
    global time_used
    global time_left

    if(not (direction in current_room['exits'])):
        return print('You cannot go there.')

    if rooms[current_room['exits'][direction]['room']]['locked']:
        return print("You can't access that room because it is locked.")


    exit_time = current_room['exits'][direction]['time']
    time_used += exit_time
    time_left -= exit_time

    current_room = move(current_room['exits'], direction)


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    selected_item = None

    for item in current_room['items']:
        if(item['id'] == item_id):
            selected_item = item
            break

    if(selected_item == None):
        return print('You cannot take that.')

    inventory.append(selected_item)
    current_room['items'].remove(selected_item)


def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """

    selected_item = None

    for item in inventory:
        if(item['id'] == item_id):
            selected_item = item
            break

    if(selected_item == None):
        return print('You cannot drop that.')

    current_room['items'].append(selected_item)
    inventory.remove(selected_item)


def execute_unlock(room_id, exits):
    """This function takes a room id as an argument and checks if the entrance can be unlocked. 
    If it can then it will be unlocked.
    """

    room_exists = False
    is_direction = False

    if room_id in rooms:
        room_exists = True

    if room_id in exits:
        room_exists = True
        is_direction = True

    if not room_exists:
        return print("That room doesn't exits.")

    is_valid_room = False

    for exit in exits:
        if is_direction:
            if exit == room_id:
                is_valid_room = True
                break
        else:
            if exits[exit]['room'] == room_id:
                is_valid_room = True
                break

    if not is_valid_room:
        return print('You cannot unlock that room from there.')

    room = None
    if not is_direction:
        room = rooms[room_id]
    else:
        room = rooms[exits[room_id]['room']]

    if room['locked'] == False:
        return print(f'{room["name"].title()} is already unlocked.')

    for item in room['required_items']:
        if not (item in inventory):
            return print(f'You cannot unlock that room without {item["name"]}.')

    room['locked'] = False
    print(f'{room["name"].title()} is unlocked.')


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "unlock":
        if len(command) > 1:
            execute_unlock(command[1], current_room['exits'])
        else:
            print("Unlock what room?")

    else:
        print("This makes no sense.")


# This is the entry point of our program
def main():

    # Main game loop
    while True:
        if(time_left <= 0):
            print('TODO: You ran out of time and SWAT stormed the bank!')
            # TODO: print user score and tier
            break

        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
