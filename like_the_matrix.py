from microbit import *
import random
####################################################################################
####### BEGIN CLASS ################################
# When called this class produces an object controls a single "drip" on the screen
class Drip():
  
  def __init__(self,startx,starty):
    self.currentx = startx
    self.low = 0
    self.high = 9
    self.mid_high_one = 6
    self.mid_high_two = 3
    self.currenty = starty
    self.trailone = starty-1
    self.trailtwo = starty-2
    self.set_all_high()
    
  def set_all_high(self):
    if self.trailtwo <= 4 and self.trailtwo >= 0:
      display.set_pixel(self.currentx,self.trailtwo,self.mid_high_two)
    if self.trailone <= 4 and self.trailone >= 0:
      display.set_pixel(self.currentx,self.trailone, self.mid_high_one)
    if self.currenty <= 4 and self.currenty >= 0:
      display.set_pixel(self.currentx,self.currenty, self.high)
  
  def set_all_low(self):
    if self.trailtwo <= 4 and self.trailtwo >= 0:
      display.set_pixel(self.currentx,self.trailtwo,self.low)
    if self.trailone <= 4 and self.trailone >= 0:
      display.set_pixel(self.currentx,self.trailone,self.low)
    if self.currenty <= 4 and self.currenty >= 0: 
      display.set_pixel(self.currentx,self.currenty,self.low)
    
    
  def increase_y_value(self):
    self.trailtwo = self.trailtwo + 1
    self.trailone = self.trailone + 1
    self.currenty = self.currenty + 1
    
    
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
