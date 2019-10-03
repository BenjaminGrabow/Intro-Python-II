from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
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

def movePlayer(direction):
  attrib = direction[0] + "_to"
  if hasattr(newPlayer.currentRoom, attrib):
    return getattr(newPlayer.currentRoom, attrib)
  else:
    return False

newPlayer = Player(room['outside'])
newPlayer.inventory.append("knife")
newPlayer.inventory.append("WaltherP99")
newPlayer.inventory.append("Dog")

while True:
  print(newPlayer.currentRoom)
  user_input = input("Choose a direction you want to go! (north / west / south / east)").strip().lower()
  if user_input == "end":
    print("Hope to see you see next time!")
    break
  elif user_input in [ "north", "west", "south", "east"] :
    if not movePlayer(user_input):
      print("You cant go in this direction from here!")
    else:
      newPlayer.currentRoom = movePlayer(user_input)
  elif user_input == "inventory":
    if len(newPlayer.inventory) == 0:
      print("You have no items !")
    else:
      print("You have items!")
      for item in newPlayer.inventory:
        print(f"\t{item}")
      print()
  else:
    print("north / south / east / west or end are valid answers!")





