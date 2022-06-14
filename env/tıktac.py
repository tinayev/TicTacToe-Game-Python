from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

y=""
x=2
player_1=[]
player_2=[]

def define_sign(number):
    global x,y
    global player_1,player_2
    
    if number==1:
       if x%2==0:
           y='X'
           player_1.appened(number)
           print(player_1)
           
    elif x%2!=0:
        y='O'
        player_2.appened(number)
        print(player_2)
    
    b1.confing(text=y)
    x=x+1
    
    if number==2:
       if x%2==0:
           y='X'
           player_1.appened(number)
           print(player_1)
           
    elif x%2!=0:
        y='O'
        player_2.appened(number)
        print(player_2)
    
    b2.confing(text=y)
    x=x+1
    
    if number==3:
       if x%2==0:
           y='X'
           player_1.appened(number)
           print(player_1)
           
    elif x%2!=0:
        y='O'
        player_2.appened(number)
        print(player_2)
    
    b3.confing(text=y)
    x=x+1
    
    if number==4:
       if x%2==0:
           y='X'
           player_1.appened(number)
           print(player_1)
           
    elif x%2!=0:
        y='O'
        player_2.appened(number)
        print(player_2)
    
    b4.confing(text=y)
    x=x+1
    
    if number==5:
       if x%2==0:
           y='X'
           player_1.appened(number)
           print(player_1)
           
    elif x%2!=0:
        y='O'
        player_2.appened(number)
        print(player_2)
    
    b5.confing(text=y)
    x=x+1
    
    if number==6:
       if x%2==0:
           y='X'
           player_1.appened(number)
           print(player_1)
           
    elif x%2!=0:
        y='O'
        player_2.appened(number)
        print(player_2)
    
    b6.confing(text=y)
    x=x+1

if number==7:
       if x%2==0:
           y='X'
           player_1.appened(number)
           print(player_1)
           
    elif x%2!=0:
        y='O'
        player_2.appened(number)
        print(player_2)
    
    b7.confing(text=y)
    x=x+1
    
    if number==8:
       if x%2==0:
           y='X'
           player_1.appened(number)
           print(player_1)
           
    elif x%2!=0:
        y='O'
        player_2.appened(number)
        print(player_2)
    
    b8.confing(text=y)
    x=x+1
    
    if number==9:
       if x%2==0:
           y='X'
           player_1.appened(number)
           print(player_1)
           
    elif x%2!=0:
        y='O'
        player_2.appened(number)
        print(player_2)
    
    b9.confing(text=y)
    x=x+1
    
    