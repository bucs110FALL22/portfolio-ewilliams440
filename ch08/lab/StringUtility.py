class StringUtility():
  def __init__(self,string):
    self.string=string

  def __str__(self):
    '''
    Returns the original string.
    args:
      self.string(str)
    returns:
      self.string(str)
    '''
    return self.string

  def vowels(self):
    '''
    Counts the number of vowels in a string, and returns "many" if the number is 5 or more.
    args:
      self.string(str)
    returns:
      vowelcount(str)
    '''
    vowels="AEIOUaeiou"
    vowelcount=0
    for i in range(len(self.string)):
      if vowelcount>4:
        return "many"
      if self.string[i] in vowels:
        vowelcount=vowelcount+1
    return str(vowelcount)

  def bothEnds(self):
    '''
    Combines the first two and last two characters of a string, or returns an empty string if the length of the original string is too short.
    args:
      self.string(str)
    returns:
      str
    '''
    if len(self.string)>2:
      return self.string[0]+self.string[1]+self.string[-2]+self.string[-1]
    else:
      return ""

  def fixStart(self):
    '''
    Replaces all the letters in a string that are the same as the first letter with "*", except for the first letter.
    args:
      self.string(str)
    returns:
      str
    '''
    if len(self.string)>1:
      letter=self.string[0]
      newstr=self.string.replace(letter,"",1)
      return letter+newstr.replace(letter,"*")
    else:
      return self.string

  def asciiSum(self):
    '''
    Sums the ASCII values of each character in the string.
    args:
      self.string(str)
    returns:
      sum(int)
    '''
    sum=0
    for i in range(len(self.string)):
      sum=sum+ ord(self.string[i])
    return sum
  
  def cipher(self):
    '''
    Encodes the string using a Caesar cipher, with a shift equal to the length of the string.
    args:
      self.string(str)
    returns:
      str
    '''
    mylist=[]
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(self.string)):
      if self.string[i] in alphabet:
        if self.string[i].isupper():
          mylist+=chr((ord(self.string[i])+len(self.string)-65)%26+65)
        else:
          mylist+=chr((ord(self.string[i])+len(self.string)-97)%26+97)
      else:
        mylist.append(self.string[i])
    return ''.join(mylist)