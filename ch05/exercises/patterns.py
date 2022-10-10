rows=int(input("Number of rows:"))
starstring="*"

def star_pyramid(rows,starstring):
  for i in range (rows):
    print(starstring*(i+1))

def rstar_pyramid(rows,starstring):
  for i in range (rows):
    print(starstring*(rows-i))

star_pyramid(rows,starstring)
print()
rstar_pyramid(rows,starstring)