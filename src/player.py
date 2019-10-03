# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, currentRoom):
    self.currentRoom = currentRoom
    self.inventory = []
  
  def get(self, item):
    self.inventory.append(item)
  
  def drop(self, item):
    self.inventory.remove(item)




