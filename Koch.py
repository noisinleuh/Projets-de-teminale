from turtle import *
from math import *

def a(): 
    clear()
    up()
    goto(-400,0)
    down()
    speed(7)



def courbe_de_Korch(dist,r):
    a()
    if r==1:
        forward(dist)
    else:
        courbe_de_Korch(dist//3, r-1)
        left(60)
        courbe_de_Korch(dist//3, r-1)
        right(120)
        courbe_de_Korch(dist//3, r-1)
        left(60)
        courbe_de_Korch(dist//3, r-1)


def flocon(dist,r):
    begin_fill()
    fillcolor("black")
    courbe_de_Korch(dist, r)
    right(120)
    courbe_de_Korch(dist, r)
    right(120)
    courbe_de_Korch(dist, r)
    end_fill()
    

"""    
    def triangle(dist,color,r):
        if r==1:
            begin_fill()
            fillcolor(color)
            for i in range(3):
                forward(dist)
                left(60)
            end_fill()
        else:
            forward(dist//2)
            left(120)
            triangle(dist//2,color,r-1)
"""

def carre(dist):
    for i in range(4):
        forward(dist)
        left(90)

def triangle(dist):
    forward(dist)
    left(150)
    forward(dist*((3**(1/2)/2)))
    left(90)
    forward(dist//2)
        
def machin(dist,r):
    if r==1:
        left(60)             
        carre(dist//2)
        right(60)
        forward(dist)
        left(60)
        carre(dist*((3**(1/2)/2)))
        right(60)
        backward(dist)        
    else:
        left(60)             
        carre(dist//2)
        left(90)
        forward(dist//2)
        right(90)
        machin(dist//2,r-1)
        right(90)
        forward(dist//2)
        left(30)
        forward(dist)
        left(60)
        carre(dist*((3**(1/2)/2)))
        forward(dist*((3**(1/2)/2)))
        left(90)
        forward(dist*((3**(1/2)/2)))
        left(180)
        machin(dist*((3**(1/2)/2)),r-1)
        right(90)
        forward(dist*((3**(1/2)/2)))
        left(90)
        forward(dist*((3**(1/2)/2)))
        left(30)
        backward(dist)
        
    
    
    
    
    
    
    
    
          
        