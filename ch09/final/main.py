from horoscope import Horoscope
from weather import Weather
from holiday import Holiday
from nextholiday import Nextholiday

def weatherweek(lat=42.09,long=-76.05):
  '''
  Prints the forecast for each day in the following week, based on location.
  args:
    lat: int
    long: int
  returns: None
  '''
  forecast=Weather(lat,long).get()
  for i in range(7):
    day=forecast[i]
    temp=day['temp2m']
    print(f"{day['date']}: {day['weather']}, high of {temp['max']}°C and low of {temp['min']}°C")

def weathertd(lat=42.09,long=-76.05):
  '''
  Prints the forecast for today based on location.
  args:
    lat: int
    long: int
  returns: None
  '''
  forecast=Weather(lat,long).get()
  day=forecast[0]
  temp=day['temp2m']
  print(f"{day['date']}: {day['weather']}, high of {temp['max']}°C and low of {temp['min']}°C")

def horoscope(sign):
  '''
  Prints the forecast for each day in the following week, based on location.
  args:
    sign: str
  returns: None
  '''
  hscp=Horoscope(sign)
  print(hscp.gethscp())

def holidays():
  '''
  Determines whether today is a holiday, or what the next holiday is.
  args: None
  returns: None
  '''
  nhy=Nextholiday().get()
  if Holiday().get()==204:
    print(f"The next holiday is {nhy}.")
  elif Holiday().get()==200:
    print(f"Today is {nhy}!")
  else:
    print("error")

def main():
  running=True
  date=Horoscope("aries").getdate()
  print("Good Morning!")
  print(f"Your Morning Overview, {date}")
  while running:
    print("\n[0] Weather \t [1] Your horoscope")
    print("[2] Holidays \t [3] Quit\n")
    displayopt=int(input())
    if displayopt==0:
      print("\n[0] Today's Weather\t[1] Weekly Forecast\n")
      displayopt=int(input())
      if displayopt==0:
        weathertd()
      elif displayopt==1:
        weatherweek()
    elif displayopt==1:
      sign=str(input("What's your sign?\n"))
      horoscope(sign)
    elif displayopt==2:
      holidays()
    elif displayopt==3:
      print("\nHave a nice day!")
      running=False

main()