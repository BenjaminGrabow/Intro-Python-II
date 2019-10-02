from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Overlook Grand", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


def chooseDirection(direction):
  if direction == "north":
    try:
      return room[str(newPlayer.currentRoom)].n_to.name.split(" ")[0].lower()
    except:
      return False
  elif direction == "south":
    try:
      return room[str(newPlayer.currentRoom)].s_to.name.split(" ")[0].lower()
    except:
      return False
  elif direction == "west":
    try:
      return room[str(newPlayer.currentRoom)].w_to.name.split(" ")[0].lower()
    except:
      return False
  elif direction == "east":
    try:
      return room[str(newPlayer.currentRoom)].e_to.name.split(" ")[0].lower()
    except:
      return False
  else:
    return False

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player('outside')

# Write a loop that:
while True:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
  print(room[str(newPlayer.currentRoom)])
# * Waits for user input and decides what to do.
  user_input = input("Choose a direction you want to go! (north / west / south / east)")
# If the user enters "q", quit the game.
  if user_input == "end":
    print("Hope to see you see next time!")
    break
# Print an error message if the movement isn't allowed.
  else:
    if not chooseDirection(user_input):
      print("""You are not able from here to go in this direction!
        north / west / south / east or end are valid answers !""")
# If the user enters a cardinal direction, attempt to move to the room there.
    else:
      newPlayer = Player(chooseDirection(user_input))



