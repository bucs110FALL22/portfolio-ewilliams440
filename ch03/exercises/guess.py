import random
answer=random.randint(1,10)

number_guesses=0
for i in range(3):
  guess=int(input("Guess a number between 1 and 10: "))
  number_guesses=number_guesses+1
  if guess==answer:
    print("correct! (", number_guesses, " guesses )")
    break
  elif guess>answer:
    print("Too High")
  else:
    print("Too Low")