import requests

class Horoscope:
  def __init__(self,sign,day="today"):
    '''
    Creates the Horoscope class, which gives a daily horoscope based on day and sign, and sets the API's url.
    args:
      self
      sign: str
      day: str
    returns: None
    '''
    self.api_url = f'https://aztro.sameerkumar.website/?sign={sign}&day={day}'

  def getdate(self):
    '''
    Returns the current date.
    args: self
    returns: str
    '''
    r=requests.post(self.api_url).json()
    return r['current_date']

  def gethscp(self):
    '''
    Returns a horoscope.
    args: self
    returns: str
    '''
    r=requests.post(self.api_url).json()
    return r['description']