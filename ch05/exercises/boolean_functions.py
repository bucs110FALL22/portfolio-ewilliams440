def percentage_to_letter(score=0):
  if score>=90:
    return ("A")
  elif score>=80:
    return ("B")
  elif score>=70:
    return ("C")
  elif score>=60:
    return ("D")
  else:
    return ("F")

def is_passing(letter=None):
  if letter=="D" or letter=="F":
    return False
  else:
    return True

grade=float(input("Score:"))
lettergrade=percentage_to_letter(grade)
r=is_passing(lettergrade)
print(r)