from turtle import *


#we want to paint house 

#step 1:  draw a square
speed(20)
begin_fill()
width(7)
color("grey")
forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)
end_fill()
#end of square

#drawing a door()
begin_fill()
forward(70)
color("brown")
left(90)
forward(100)   #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()
#end of door
#draw a triangle
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of triangle

#start a 1 windows
penup()
goto(15, 170)
pendown()

color("blue")
begin_fill()


left(30)
forward(50)

left(90)
forward(50)

left(90)
forward(50)
left(90)
forward(50)
end_fill()
#end of 1 window

#start a 2 window
color("blue")
begin_fill()
penup()
goto(180, 170)
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
#end of house

print("es aris saxli")


exitonclick()