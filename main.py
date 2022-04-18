# -*- coding: utf-8 -*-
"""
@author: krishivg
"""

# Import libraries. Turtle for drawing. cv for image. tk for page. time for delay. 
import turtle as t
import cv2 as cv 
import time
#Create class for rocks.


class Rock:
    def __init__(self, name):
        self.name = name


sRock = Rock("Sedimentary")
iRock = Rock("Igneous")
mRock = Rock("Metemorphic")

# Create starting page & take rockchoice value.
t.setup (1500,1500)
t.bgcolor('DarkBlue')
try:
    rockchoice = t.textinput("What rock do you want to learn about?", "Igneous, Metamorphic, or Sedimentary")
except (ValueError):
    rockchoice = sRock
#Starting page:
t.pencolor("White")
t.speed(3)
t.penup()
t.goto(x=-600,y=600)
t.pendown()
t.write("Did you know that Rocks change?! (You probably did)", font =('Arial', 18, "bold"))
t.penup()
t.goto(-600, y=400)
t.pendown()
t.color ('white')
t.write("Let's find out how rocks change! We'll also look at 3 types of rock!", font =('Arial', 15, "bold"))
t.color ('chocolate')
t.penup()
t.goto (-750,-300)
t.pendown()
t.begin_fill ()
for i in range (2):
    t.forward (1500)
    t.right (90)
    t.forward (450)
    t.right (90)
t.end_fill ()    
t.penup()
t.goto(-550,-299)
t.pendown()
t.color('white')
t.begin_fill()
for m in range (1):
    for x in range (3):
        t.right(-60)
        t.forward(200)
        t.right(120)
        t.forward(200)
        t.right(-60)
    t.right(180)
    t.forward(610)
t.end_fill ()
time.sleep(7)
 
 
if rockchoice == "Igneous":
    rockchoice = iRock
elif rockchoice == "Metamorphic":
    rockchoice = mRock
else:
    rockchoice = sRock
#
#
#
# give rock values
rocksdict = {
    "Sedimentary": sRock,
    "Igneous": iRock,
    "Metamorphic": mRock
    }
if rockchoice == iRock:
    iRockvalue = True
    mRockvalue = False
    sRockvalue = False
elif rockchoice == mRock:
    iRockvalue = False
    mRockvalue = True
    sRockvalue = False
else:
    rockchoice = sRock
    mRockvalue = False
    iRockvalue = False
    sRockvalue = True
sRockcompletion = 0
iRockcompletion = 0
mRockcompletion = 0
# Run sedimentary code if sRockvalue = True
while sRockvalue is True and sRockcompletion == 0:
    #sRockbody
    t.clear()
    t.bgcolor('springgreen')
    t.color('black')
    t.penup()
    t.goto(-200,500)
    t.pendown()
    t.write("Sedimentary Rocks", font =("Arial", 20, "bold"))
    t.penup()
    t.goto(-500,300)
    t.pendown()
    t.write('''A type of rock that is quite cool are Sedimentary rocks!!!
In fact these rocks can take millions of years to form.
They compose 5% of rocks''', font =('Arial', 15))
    t.penup()
    t.speed(8)
    t.goto(-100,-925)
    t.right(15)
    t.color('gray45')
    t.begin_fill()
    for y in range (2):
        t.forward(800)
        t.right(90)
        t.forward(250)
        t.right(90)
    t.end_fill()
    t.up()
    t.goto(-150,-400)
    t.down()
    t.left(10)
    t.begin_fill()
    t.color('gray60')
    for z in range(2):
        t.forward(-1200)
        t.right(90)
        t.forward(-300)
        t.right(90)
    t.end_fill()
    t.up()
    t.right(0)
    t.goto(700,-480)
    t.color('mediumpurple1')
    t.down()
    t.begin_fill()
    for l in range (1):
        for r in range (4):
            t.right(60)
            t.forward(200)
            t.right(-120)
            t.forward(200)
            t.right(60)
        t.right(180)
        t.forward(610)
    t.end_fill()
    t.up()
    t.goto(-900,-400)
    t.color('dodgerblue1')
    t.down()
    t.begin_fill()
    for d in range (2):
        t.forward(800)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()
    t.up()
    t.goto(-600,200)
    t.color('black')
    t.down()
    t.write('Energy from the sun causes weathering, making sediments (2 million years)', font = ('Arial', 12, 'bold'))
    time.sleep(3)
    t.speed(20)
    t.shape('circle')
    t.up()
    t.goto(-700,-590)
    t.down()
    for e in range (35):
        t.forward(15)
        t.dot()
    t.up()
    t.goto(-600,0)
    t.down()
    time.sleep(1)
    t.write('''Compaction & Cementation happens when sediments weight causes them to compact,
and then the minerals in water between grains crystalize, gluing them together.
(A few thousand years)''', font = ('Arial', 12, 'bold'))
    time.sleep(2)
    t.up()
    t.goto(-670,-600)
    t.begin_fill()
    for c in range (2):
        t.forward(500)
        t.right(90)
        t.forward(30)
        t.right(90)
    t.end_fill()    
    time.sleep(8)
    print("Test A")
    sRockcompletion = sRockcompletion+1
    sRockvalue = False
    iRockvalue = True
    
# Run iRock code
while iRockvalue is True and iRockcompletion == 0:
    #iRockbody
    t.clear()
    t.bgcolor('Red')
    t.up()
    t.goto(-200,600)
    t.down()
    t.write('Igneous Rock', font = ("Arial", 20, "Bold"))
    t.up()
    t.goto(-400,400)
    t.down()
    t.write("""Igneous Rock happen near volcanos,
and consist of 15% of rocks.
They only take a few minutes to form.""", font = ("Arial", 15, "Bold"))
    t.up()
    t.goto(-750,-300)
    t.down()
    t.begin_fill()
    for b in range(2):
        t.forward(1500)
        t.right(90)
        t.forward(300)
        t.right(90)
    t.end_fill()
    t.up()
    t.goto(-300,200)
    t.down()
    t.write('First melted rock (magma becoming lava) comes to the surface.', font = ('Arial', 15, 'bold'))
    t.up()
    t.goto(0,-750)
    t.left(90)
    t.color('red')
    t.begin_fill()
    for j in range (2):
        t.forward(450)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()
    t.up()
    t.goto(-300,0)
    t.down()
    t.color('black')
    time.sleep(2)
    t.write('Then the lava cools, making igneous rock!!!', font = ('Arial', 15, 'bold'))
    t.up()
    t.goto(0,-299)
    t.begin_fill()
    t.left(90)
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.sleep(8)
    print('Test B')
    iRockcompletion = iRockcompletion+1
    iRockvalue = False
    mRockvalue = True
# Run mRock code
while mRockvalue is True and mRockcompletion == 0:
    # mRockbody
    t.clear()
    print("Test C")
    mRockcompletion = mRockcompletion+1
    mRockvalue = False
#if mRockcompletion != 0 and sRockcompletion != 0 and iRockcompletion != 0:

