class Temperature:
  def __init__(self,c):
    self.cel=c

  @property
  def celsius(self):
        return self.cel
  @property
  def fahrenheit(self):
        return (self.cel*1.8)+32
  
  @fahrenheit.setter
  def fahrenheit(self,f):
        self.cel=(5/9)*(f-32)
        

if __name__ == '__main__':
    t = Temperature(0)
    print(t.fahrenheit)   # 32
    t.fahrenheit = 212
    print(t.celsius)      # 100

    

