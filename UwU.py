#===============================================================================#
#                            # February Assignment #                            #
#                             =------------------=                              #  
#                                                                               #  
#                               Shiven Viddemari                                #
#                               Due: 14/02/2021                                 #
#                                                                               #
#===============================================================================#





#------------------------Part One and Two Resources-----------------------------#

day_one_temp = [
  
  4.5,4.2,4,3.2,2.5,1.9,2.8,3,2.3,1.7,2,3.6,4.5,5,5.7,5.4,5.1,4.3,3.1,3,2.5,1.7,1.5,1.2
  
  ]


day_two_temp = [
  
  1.1,0.6,0.1,0.3,0.4,0.8,1.3,1.4,1.3,1.3,1.4,1.7,1.9,2.6,2.2,2.8,2.1,0.7,0,-0.3,-0.6,-1.1,-1.2,-1.5
  
  ]


day_three_temp = [

  -1.4,-1.4,-1.3,-1.5,-1.6,-1.2,-1.5,-1.4,-0.6,-0.4,0.3,0.7,1.9,2.5,2.1,2.4,2.1,2.4,3.2,3.9,4.2,4.4,4.4,4.5
  
  ]






day_one_rainfall = [

  0,0,0.1,0.3,0,0.1,0.2,0.6,1.1,3.4,0.7,0,0,0,0,0,0,0,0,0.5,2.2,1.3,0.3,0
  
  ]


day_two_rainfall = [

  0,0,0,0,0,0,0,0.1,0.5,0.2,0,0,0.1,0.3,1.7,0.9,0.4,0.1,0,0,0,0,0,0
  
  ]


day_three_rainfall = [

  0.3,0.2,0.1,1.3,0,0,0.6,0,0.1,0.2,0.3,0.4,2.4,0,0,0.5,0,0.1,0,0.8,0.1,0,0.1,0.8
  
  ]

#---------------------------Packages and Miscallaneous--------------------------#

from os import system, name
from numpy import *
from statistics import *
from time import sleep


def clear():                                  
    if name == 'nt':                                 
        _ = system('cls')      
    else:                          
        _ = system('clear')




class colors:
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'     
    red = '\033[91m'
    white = '\033[0m'  
    bold = '\033[1m'
    underline = '\033[4m'


#-------------------------------------------------------------------------------#

print(colors.purple + colors.bold + colors.underline + "Welcome to my February Assignment")
sleep(1)
print("")
print(colors.white + "Which part do you want to view? (Part 1-3) ")
sleep(1)
print("")
part_menu_init = int(input("Part " + colors.purple))  
sleep(1)
clear()
print("")
print("")


if part_menu_init == 1:
  print(colors.white + "Which question in part 1?")
  sleep(0.5)
  print("" + colors.green)
  print("Question 1 ->\nQuestion 2 ->\nQuestion 3 ->\nQuestion 4 ->\nQuestion 5 ->")
  print("" + colors.white)
  part_1_questions = int(input("Question " + colors.purple))
  











