# create flower by python 🐢 by Smruti official

import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')
Smruti = turtle.Turtle()
Smruti.speed(0)
Smruti.color('white')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(Smruti,100,10)
kitu = turtle.Turtle()
kitu.speed(0)
kitu.color('yellow')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(kitu,100,10)
Gudu = turtle.Turtle()
Gudu.speed(0)
Gudu.color('blue')
rotate=int(80)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Gudu,100,10)
Asu = turtle.Turtle()
Asu.speed(0)
Asu.color('orange')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Asu,100,10)
Sipun = turtle.Turtle()
Sipun.speed(0)
Sipun.color('Red')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Sipun,100,10)