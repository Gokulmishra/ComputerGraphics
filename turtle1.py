#import win10toast // library for desktop  notification
#from win10toast import ToastNotifier // not required for graphics
#n = ToastNotifier() // same

from turtle import *
from random import randint
bgcolor('black')
red=[210,0,0,255,255,255]
green=[0,128,0,128,255,255]
blue=[0,128,128,0,0,255]


red1=[0,128,150,255]
blue1=[0,128,150,255]
green1=[0,128,150,255]
#m=int(input("Enter the size "))
#s=int(input("Enter the speed "))

x=j=10
speed(200)
pensize(5)

while x < (410):
 
 
 
 colormode(255)
 pencolor((red[x % 6]),(green[x % 6]),(blue[x % 6])) // # for square pattern

 #pencolor((red[x % 4]),(green[x % 4]),(blue[x % 4])) //remove # for square pattern // change rt(60.5) to rt(90.5) for square
 
 fd(30+x)
 rt(60.5)   
 x = x+1
 

#n.show_toast("Your Name", "Your program got executed", duration = 20) // for desktop Notification 

exitonclick()
