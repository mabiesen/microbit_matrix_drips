from microbit import *
import random

class drip():
  low = 0
  high = 9
  
  def __init__(self):
    self.currentx = random.choice(0,4)
    self.currenty = 0
    self.trailone = currenty - 1
    self.trailtwo = currenty - 2

  def move_trail_one(self):
    display.set_pixel(self.currentx,self.trailone,low)
    self.trailone = self.trailone + 1
    display.set_pixel(self.currentx,self.trailone,high)

  def move_trail_two(self):
    display.set_pixel(self.currentx,self.trailtwo,low)
    self.trailtwo = self.trailtwo + 1
    display.set_pixel(self.currentx,self.trailtwo,high)

  def move_current(self):
    display.set_pixel(self.currentx,self.currenty,low)
    self.currenty = self.currenty + 1
    display.set_pixel(self.currentx,self.currety,high)
