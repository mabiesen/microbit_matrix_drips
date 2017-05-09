from microbit import *
import random
####################################################################################
####### BEGIN CLASS ################################


# When called this class produces an object that represents a single "drip" on the screen
# Our drip consists of 3 datasets representing led coordinates, with the first(lowest) being the brightest and the last being the dimmest
class Drip():
  
  # the __init__ function is a python built in function that is immediately called when an object is created
  def __init__(self,startx,starty):     # Arguments passed during class call used here. starting y values can be negative
    # set led brightness levels
    self.low = 0
    self.high = 9
    self.mid_high_one = 6
    self.mid_high_two = 3
    
    # set starting x and y coordinates
    # Note:  "Current" represents the first led, "trailone" the next led, and "trailtwo" the last led
    self.currentx = startx
    self.currenty = starty
    self.trailone = starty-1
    self.trailtwo = starty-2
    
    # call our leds to turn on.  
    self.set_all_high()
  
  # Set each of the three leds to their brightness level if coordinates fall on the led display
  def set_all_high(self):
    if self.trailtwo <= 4 and self.trailtwo >= 0:
      display.set_pixel(self.currentx,self.trailtwo,self.mid_high_two)
    if self.trailone <= 4 and self.trailone >= 0:
      display.set_pixel(self.currentx,self.trailone, self.mid_high_one)
    if self.currenty <= 4 and self.currenty >= 0:
      display.set_pixel(self.currentx,self.currenty, self.high)
  
  # Turn off each of the leds if theyir coordinates fall on the led display
  def set_all_low(self):
    if self.trailtwo <= 4 and self.trailtwo >= 0:
      display.set_pixel(self.currentx,self.trailtwo,self.low)
    if self.trailone <= 4 and self.trailone >= 0:
      display.set_pixel(self.currentx,self.trailone,self.low)
    if self.currenty <= 4 and self.currenty >= 0: 
      display.set_pixel(self.currentx,self.currenty,self.low)
    
  # This increases the led y value coordinates, thereby moving the drip down the screen  
  def increase_y_value(self):
    self.trailtwo = self.trailtwo + 1
    self.trailone = self.trailone + 1
    self.currenty = self.currenty + 1
    
 # This is our container function for drip actions.   
  def move_the_drip(self):
    self.set_all_low()
    self.increase_y_value()
    self.set_all_high()

############### END CLASS #######################################
#################################################################################

#################################################################
################## Tester functions #####################################   

def one_at_a_time():
    while True:
      startx = random.randint(0,4)
      myobject = Drip(startx)
      while myobject:
        if myobject.currenty > 7:
          del myobject
          break
        else:
          myobject.move_the_drip()
          sleep(100)

# Delayed image for each dripped is achieved by providing negative y values during class call
def waterfall():
    while True:
        first = Drip(0,0)
        second = Drip(1,-2)
        third = Drip(2,-4)
        fourth = Drip(3,-6)
        fifth = Drip(4,-8)
        my_water = [first,second,third,fourth,fifth]
        while True:
            for water in my_water:
                water.move_the_drip()
            if my_water[-1].currenty > 7:
                break
            sleep(300)
        
      
          
######################## END TESTER FUNCTIONS ######################################
#################################################################################

# kick off program
waterfall()
