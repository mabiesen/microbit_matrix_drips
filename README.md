# Make an led screen like in The Matrix

WIP

You know how in the Matrix 0s and 1s go running down the screen? Well, we can do something similar in the microbit.

I am going to create a drip class that will be used to create our drip objects. 

```
from microbit import *
import random

class drip():
  low = 0
  high = 9
  
  def __init__(self):
    self.currentx = random.choice(0,4)
    self.currenty = 0
    self.trailone = 0
    self.trailtwo = 0

  def turn_off():

  def turn_on():

  def move_trail_one():
    
  def move_trail_two():

  def move_current(self):
    display.set_pixel(self.currentx,self.currenty,low)
    self.currenty = self.currenty + 1
    display.set_pixel(self.currentx,self.currety,high)
    
  
```
