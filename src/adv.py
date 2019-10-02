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

newPlayer = Player('outside')

print(room[str(newPlayer.currentRoom)])

endTheGame = True

def chooseDirection(direction):
  if direction == "north":
    # if room[str(newPlayer.currentRoom)]:
    #   print(room[str(newPlayer.currentRoom)].n_to)
    #   return room[str(newPlayer.currentRoom)].n_to.name.split(" ")[0].lower() 
    # else:
    #   return print("You are not able from here to go in this direction!")
    try:
      print(room[str(newPlayer.currentRoom)].n_to)
      return room[str(newPlayer.currentRoom)].n_to.name.split(" ")[0].lower()
    except:
      # print("You are not able from here to go in this direction!")
      return False
  elif direction == "south":
    # if room[str(newPlayer.currentRoom)].s_to:
    #   print(room[str(newPlayer.currentRoom)].s_to)
    #   return room[str(newPlayer.currentRoom)].s_to.name.split(" ")[0].lower()
    # else:
    #   return print("You are not able from here to go in this direction!")
    try:
      print(room[str(newPlayer.currentRoom)].s_to)
      return room[str(newPlayer.currentRoom)].s_to.name.split(" ")[0].lower()
    except:
      # print("You 0are not able from here to go in this direction!")
      return False
  elif direction == "west":
    # if room[str(newPlayer.currentRoom)].w_to:
    #   print(room[str(newPlayer.currentRoom)].w_to)
    #   return room[str(newPlayer.currentRoom)].w_to.name.split(" ")[0].lower()      
    # else:
    #   return print("You are not able from here to go in this direction!")
    try:
      print(room[str(newPlayer.currentRoom)].w_to)
      return room[str(newPlayer.currentRoom)].w_to.name.split(" ")[0].lower()
    except:
      # print("You are not able from here to go in this direction!")
      return False
  elif direction == "east":
    # if room[str(newPlayer.currentRoom)].e_to:
    #   print(room[str(newPlayer.currentRoom)].e_to)
    #   return room[str(newPlayer.currentRoom)].e_to.name.split(" ")[0].lower()
    # else:
    #   return print("You are not able from here to go in this direction!")
    try:
      print(room[str(newPlayer.currentRoom)].e_to)
      return room[str(newPlayer.currentRoom)].e_to.name.split(" ")[0].lower()
    except:
      # print("You are not able from here to go in this direction!")
      return False
  else:
    return print("This is no valid direction!")
  
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
#CODE HERE
# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#CODE HERE

while True:
  user_input = input("Choose a direction you want to go! (north / west / south / east)")
  if user_input == "end":
    print("Hope to see you see next time!")
    break
  else:
    if not chooseDirection(user_input):
       print("You are not able from here to go in this direction!")
    else:
       newPlayer = Player(chooseDirection(user_input))

# If the user enters a cardinal direction, attempt to move to the room there.
#CODE HERE

# Print an error message if the movement isn't allowed.
#CODE HERE

# If the user enters "q", quit the game.
