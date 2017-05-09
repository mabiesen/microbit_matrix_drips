from microbit import *
import random

class Drip():
  low = 0
  high = 9
  mid_high_one = 3
  mid_high_two = 6
  
  def __init__(self):
    self.currentx = random.choice(0,4)
    self.currenty = 0
    self.trailone = currenty - 1
    self.trailtwo = currenty - 2
  
  def set_all_low(self):
    display.set_pixel(self.currentx,self.trailtwo,low)
    display.set_pixel(self.currentx,self.trailone,low)
    display.set_pixel(self.currentx,self.currenty,low)
    
    
  def increase_y_value(self):
    self.trailtwo = self.trailtwo + 1
    self.trailone = self.trailone + 1
    self.currenty = self.currenty + 1
  
  def move_trail_two(self):
    if self.trailtwo <= 4 and self.trailtwo >= 0:
      display.set_pixel(self.currentx,self.trailtwo,mid_high_two)

  def move_trail_one(self):
    if self.trailtwo < 4 and self.trailtwo >= 0:
      display.set_pixel(self.currentx,self.trailone,mid_high_one)

  def move_current(self):
    if self.trailtwo < 4 and self.trailtwo >= 0:
      display.set_pixel(self.currentx,self.currety,high)
    
  def move_all(self):
    self.set_all_low()
    self.move_current()
    self.move_trailone()
    self.move_trailtwo()
    
def main():
  myobject = Drip()
  while myobject():
    
  
    

