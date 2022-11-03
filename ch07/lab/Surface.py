from Rectangle import Rectangle

class Surface:
    def __init__(self, filename, x, y, h, w):
     self.image=filename
     self.rect=Rectangle(x,y,h,w)
    def getRect(self):
      '''
      Returns a Rectangle object.
      args:
        self.rect(Rectangle)
      returns:
        self.rect(Rectangle)
      '''
      return self.rect