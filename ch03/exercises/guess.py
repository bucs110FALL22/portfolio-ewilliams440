import random
answer=random.randint(1,10)

for i in range(3):
  guess=int(input("Guess a number between 1 and 10: "))
  if guess==answer:
    print("correct!")
    break;
  elif guess>answer:
    print("Too High")
  else:
    print("Too Low")