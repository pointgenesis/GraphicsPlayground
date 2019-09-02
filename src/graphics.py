'''
Created on Sep 1, 2019

@author: travis l. steinmetz

References: 

[1] http://openbookproject.net/thinkcs/python/english3e/genindex.html
'''

import turtle

#------------------------------------------------------------------------------  
def draw_concentric_squares(draw, length):

    while length > 0:
        draw.pd()
        
        print('current value of length: ' + str(length))
        
        sides = 4
        while sides > 0:
            draw.fd(length)
            draw.lt(90)
            
            sides = sides - 1
            
        draw.pu()
        
        spacer = 10
        
        draw.lt(90)
        draw.fd(spacer)
        draw.rt(90)
        draw.fd(spacer)
        
        length = length - (2 * spacer)
        
    print(draw)


#------------------------------------------------------------------------------
def polygon(draw, sides, length):
    draw.fd(200)
    draw.pd()
    
    angle = 360/sides
    
    for i in range(sides):
        print('current iteration -> i: ' + str(i))
        draw.fd(length)
        draw.lt(angle)

#------------------------------------------------------------------------------
def mystery(draw, length, order):
    if order == 0:
        return 
    
    angle = 50
    draw.fd(length*order)
    draw.lt(angle)
    
    mystery(draw, length, order - 1)
    draw.rt(2*angle)
    
    mystery(draw, length, order - 1)
    draw.lt(angle)
    draw.bk(length*order)

#------------------------------------------------------------------------------
def koch(draw, order, size):
    '''
    Creaetes a Kock Curve (fractal) with the given parameters.
    
    t - turtle drawing instrument
    order - Kock curve order, i.e. levels of recursion. Order-0 is a straight line, Order-1 is a _/|_ line, etc.
    size - line length
    '''
    if order == 0:
        draw.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(draw, order-1, size/3)
            draw.left(angle)
          
#------------------------------------------------------------------------------
'''
Test what we have written...
'''
instrument = turtle.Turtle()
instrument.hideturtle()
    
draw_concentric_squares(instrument, 100)

polygon(instrument, 7, 70)
polygon(instrument, 100, 2)

instrument.penup()
instrument.back(1000)
instrument.pencolor('red')
instrument.pendown()
mystery(instrument, 10, 5)

instrument.penup()
instrument.forward(200)
instrument.pencolor('blue')
instrument.pendown()

koch(instrument, 7, 10000)

win = turtle.Screen()
win.mainloop()