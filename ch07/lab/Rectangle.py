class Rectangle:
  def __init__(self,x,y,h,w):
    if x>0:
      self.x=x
    else:
      self.x=0
    if y>0:
      self.y=y
    else:
      self.y=0
    if h>0:
      self.height=h
    else:
      self.height=0
    if w>0:
      self.width=w
    else:
      self.width=0

  def __str__(self):
    '''
    Takes the x, y, width, and height parameters and returns them in a string.
    args:
      self.x(int)
      self.y(int)
      self.height(int)
      self.width(int)
    returns: str
    '''
    return f"(x:{self.x}, y:{self.y}) width:{self.width}, height:{self.height}"