import requests

class Weather:
  def __init__(self,lat=42.09,long=-76.05):
    '''
    Creates the Weather class, which returns the weather forecast for the week, and sets the API's url.
    args:
      self
      lat: int
      long: int
    returns: None
    '''
    self.api_url= f'http://www.7timer.info/bin/api.pl?lon={long}&lat={lat}&product=civillight&output=json'

  def get(self):
    '''
    Creates the Weather class, which returns the weather forecast for the week, and sets the API's url.
    args: self
    returns: str
    '''
    r=requests.post(self.api_url).json()
    return r['dataseries']