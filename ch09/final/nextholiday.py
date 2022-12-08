import requests

class Nextholiday:
  def __init__(self,country="US"):
    '''
    Creates the Nextholiday class, which determines the closest holiday, and sets the API's url.
    args:
      self
      country: str
    returns: None
    '''
    self.api_url= f'https://date.nager.at/api/v3/NextPublicHolidays/{country}'

  def get(self):
    '''
    Returns the closest holiday
    args: self
    returns: str
    '''
    r=requests.get(self.api_url).json()
    next=r[0]
    return next['localName']