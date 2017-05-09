from microbit import *
import random

class drip():
  low = 0
  high = 9
  mid_high_one = 3
  mid_high_two = 6
  
  def __init__(self):
    self.currentx = random.choice(0,4)
    self.currenty = 0
    self.trailone = currenty - 1
    self.trailtwo = currenty - 2
    
  def move_trail_two(self):
    display.set_pixel(self.currentx,self.trailtwo,low)
    if self.trailtwo <= 4 and self.trailtwo >= 0:
      self.trailtwo = self.trailtwo + 1
      display.set_pixel(self.currentx,self.trailtwo,mid_high_two)

  def move_trail_one(self):
    display.set_pixel(self.currentx,self.trailone,low)
    if self.trailtwo < 4 and self.trailtwo >= 0:
      self.trailone = self.trailone + 1
      display.set_pixel(self.currentx,self.trailone,mid_high_one)

  def move_current(self):
    display.set_pixel(self.currentx,self.currenty,low)
    self.currenty = self.currenty + 1
    display.set_pixel(self.currentx,self.currety,high)
    
  def move_all(self):
    self.move_current()
    self.move_trailone()
    self.move_trailtwo()
    

    

