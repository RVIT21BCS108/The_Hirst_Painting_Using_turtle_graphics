import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle() # draws without showing the turtle object
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)] # a list of tuples showing RGB color values 

tim.setheading(225) #Points the turtle 225 degrees (down-left) tobring turtle to starting position that is centre of screen 

tim.forward(300) #Moves the turtle 300 units forward in the 225-degree direction. This ensures that the turtle starts from a position that allows for sufficient space to draw the entire grid of dots within the window.

tim.setheading(0) # Points the turtle to the right (0 degrees), ready to start drawing the first row of dots.

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1): # to draw 100 dots
    tim.dot(20, random.choice(color_list)) # Draws a dot with a diameter of 20 units and a randomly chosen color from color_list.
    
    tim.forward(50) 

    if dot_count % 10 == 0: # after every 10 dots
        tim.setheading(90) # points the turtle up(90 degrees)
        tim.forward(50) #move turtle up by 50 units
        tim.setheading(180) #Points the turtle to the left (180 degrees).
        tim.forward(500)# Moves the turtle to the left by 500 units, positioning it at the start of the next row.
        tim.setheading(0) # Points the turtle to the right (0 degrees) to start drawing the next row of dots.

screen = turtle_module.Screen()
screen.exitonclick()
