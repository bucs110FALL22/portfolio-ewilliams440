import time

class Animal:
  def __init__(self,name,type="dog"):
    self.id=id(name)
    self.name=name
    self.type=type
    self.arrived=time.strftime("%d/%m/%Y")
    self.adopted=None
  def adoption(self):
    self.adopted=time.strftime("%d/%m/%Y")

def main():
  fido=Animal("Fido")
  luna=Animal("Luna","cat")
  fido.adoption()

main()