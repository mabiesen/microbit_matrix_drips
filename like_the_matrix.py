from microbit import *
import random

class Drip():
  low = 0
  high = 9
  mid_high_one = 6
  mid_high_two = 3
  
  def __init__(self):
    self.currentx = random.choice(0,4)
    self.currenty = 0
    self.trailone = currenty - 1
    self.trailtwo = currenty - 2
    self.light_up_all()
  
  def set_all_low(self):
    if self.trailtwo <= 4 and self.trailtwo >= 0:
      display.set_pixel(self.currentx,self.trailtwo,low)
    if self.trailtwo < 4 and self.trailtwo >= 0:
      display.set_pixel(self.currentx,self.trailone,low)
    if self.currenty < 4 and self.currenty >= 0: 
      display.set_pixel(self.currentx,self.currenty,low)
    
    
  def increase_y_value(self):
    self.trailtwo = self.trailtwo + 1
    self.trailone = self.trailone + 1
    self.currenty = self.currenty + 1
    
  def set_all_high():
    if self.trailtwo <= 4 and self.trailtwo >= 0:
      display.set_pixel(self.currentx,self.trailtwo,mid_high_two)
    if self.trailone < 4 and self.trailone >= 0:
      display.set_pixel(self.currentx,self.trailone,mid_high_one)
    if self.currenty < 4 and self.currenty >= 0:
      display.set_pixel(self.currentx,self.currety,high)
    
    
  def move_the_drip():
    self.set_all_low()
    self.increase_y_value()
    self.set_all_high()
    
while True:
  myobject = Drip()
  while myobject:
    if myobject.currenty == 6:
      del myobject
    else:
      myobject.move_the_drip()
      sleep(200)
    
  
    

