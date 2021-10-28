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

# Either the variable of the room it is planted in or None
bomb_plant_location = None

game_ended = False


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.
    """

    # Display menu
    # print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def execute_go(direction, isGo):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    global current_room
    global time_used
    global time_left
    global game_ended

    if(not (direction in current_room['exits'])):
        return print(f"You cannot {'go there' if isGo else 'enter that'}.")

    if rooms[current_room['exits'][direction]['room']]['locked']:
        return print(f"You can't access that{' room' if isGo else ''} because it is locked.")

    exit_time = current_room['exits'][direction]['time']
    time_used += exit_time
    time_left -= exit_time

    current_room = move(current_room['exits'], direction)

    escape_rooms = [rooms['sewage'], rooms['exit'],
                    rooms['van'], rooms['helicopter']]
    if current_room in escape_rooms:
        print_room(current_room)
        game_ended = True


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    global bomb_plant_location

    selected_item = None

    for item in current_room['items']:
        if(item['id'] == item_id):
            selected_item = item
            break

    if(selected_item == None):
        return print('You cannot take that.')

    # If taking the bomb change the name
    if selected_item['id'] == 'bomb':
        selected_item['name'] = 'the bomb'
        bomb_plant_location = None

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
        return print("That place doesn't exits.")

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
        return print('You cannot unlock that place from there.')

    room = None
    if not is_direction:
        room = rooms[room_id]
    else:
        room = rooms[exits[room_id]['room']]

    if room['locked'] == False:
        return print(f'{capitalise_sentence(room["name"])} is already unlocked.')

    for item in room['required_items']:
        if not (item in inventory):
            return print(f'You cannot unlock that place without {item["name"]}.')

    room['locked'] = False
    print(f'{capitalise_sentence(room["name"])} is unlocked.')


def execute_plant(item_id):
    global bomb_plant_location
    global time_used
    global time_left

    if item_id != 'bomb':
        return print("You can't plant that.")

    item = items[item_id]

    if not (item in inventory):
        return print("You don't have that.")

    item['name'] = 'the planted bomb'
    bomb_plant_location = current_room
    inventory.remove(item)
    current_room['items'].append(item)

    # Implement time used to plant bomb
    time_used += 30
    time_left -= 30

    print(
        f'The bomb is planted in {capitalise_sentence(current_room["name"])}.')


def execute_detonate(item_id):
    global bomb_plant_location
    global game_ended

    if item_id != 'bomb':
        return print("You can't detonate that.")

    if bomb_plant_location == None:
        return print("The bomb is not planted.")

    if current_room == bomb_plant_location:
        game_ended = True
        return print('You detonated the bomb in the same room as yourself and got blown up.')

    end_words = ''

    if bomb_plant_location == rooms['armoury']:
        end_words = 'and opened up a hole in the wall to the east'
        new_exit = {
            'room': 'sewage',
            'time': 0,
        }
        rooms['armoury']['exits']['east'] = new_exit
    else:
        end_words = 'and did nothing'

    bomb_plant_location['items'].remove(items[item_id])

    print(
        f'The bomb has been detonated in {capitalise_sentence(bomb_plant_location["name"])} {end_words}.')

    bomb_plant_location = None


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    """

    if 0 == len(command):
        return

    if command[0] == "go" or command[0] == "enter":
        if len(command) > 1:
            execute_go(command[1], command[0] == "go")
        else:
            if command[0] == "go":
                print("Go where?")
            else:
                print("Enter what?")

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

    elif command[0] == "plant":
        if len(command) > 1:
            execute_plant(command[1])
        else:
            print("Plant what?")

    elif command[0] == "detonate":
        if len(command) > 1:
            execute_detonate(command[1])
        else:
            print("Detonate what?")

    elif command[0] == "h" or command[0] == "help":
        print_helpers()

    else:
        print("This makes no sense.")


# This is the entry point of our program
def main():

    # TODO: main menu screen
    print('\nMAIN MENU SCREEN')

    while True:
        # TODO: main menu options
        print('\nMAIN MENU OPTIONS (Play (P), Help(H), Leader Board(L), Quit(Q))\n')
        menu_input = str(input("> "))
        if menu_input.lower().strip() == 'p':
            break
        elif menu_input.lower().strip() == 'h':
            print_helpers()
        elif menu_input.lower().strip() == 'l':
            # TODO: leaderboard screen
            print('\nLEADER BOARD SCREEN')
        elif menu_input.lower().strip() == 'q':
            return
        else:
            pass

    # TODO: intro text
    print('\nGAME INTRO TEXT')

    # Main game loop
    while True:
        if(time_left <= 0):
            print('TODO: You ran out of time and SWAT stormed the bank!')
            # TODO: print user score and tier
            break

        # Display game status (room description, inventory etc.)
        print_room(current_room)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

        if game_ended:
            # TODO: print user score and tier
            break


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
