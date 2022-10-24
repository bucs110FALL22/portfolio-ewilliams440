class MysteryBlock:
  def __init__(self):
    self.is_activated=False #block hasn't been activated yet
    self.type_of_block="coin" #the block will give mario one coin once activated
    self.location=(1,2) #where the block appears on screen/hitbox

class Goomba1:
  def __init__(self):
    self.goomba=1 #first goomba
    self.is_dead=False #hasn't been killed by mario
    self.movement="left" #which direction the goomba is moving
    self.location=(3,4) #location

class Goomba2:
  def __init__(self):
    self.goomba=2 #second goomba
    self.is_dead=False #hasn't been killed by mario
    self.movement="right" #which direction the goomba is moving
    self.location=(5,6) #location
    