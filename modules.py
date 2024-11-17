   #importing a created module
import my_module
print(my_module.greet("jatelo"))

   #importing modules
import math
print(math.cos(70))

  #renaming  modules
import math as m
print(m.log(7)) 

#importing specific functions from a module
from math import lcm
print(lcm(7,8,9))