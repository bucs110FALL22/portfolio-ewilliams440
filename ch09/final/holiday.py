import requests

class Holiday:
  def __init__(self,country="US"):
    '''
    Creates the Holiday class,which checks if today is a holiday, and sets the API's url.
    args:
      self
      country: str
    returns: None
    '''
    self.api_url= f'https://date.nager.at/api/v3/IsTodayPublicHoliday/{country}?offset=0'

  def get(self):
    '''
    Returns a status code depending on whether or not today is a holiday.
    args: self
    returns: int
    '''
    r=requests.get(self.api_url)
    return r.status_code