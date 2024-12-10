import turtle




screen = turtle.Screen()


screen.setup(800, 800)


screen.bgcolor('Cornflower blue')
t = turtle.Turtle()
t.showturtle()
t2 = turtle.Turtle()
t2.showturtle()
t3 = turtle.Turtle()
t3.showturtle()
t3.hideturtle()


t.hideturtle()
t2.hideturtle()


t.speed(2000)
t.penup()
t.goto(-50,0)
t.pendown()
t.fillcolor("purple")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()


t2.penup()
t2.goto(0, 100)
t2.pendown()
t3.penup()
t3.goto(0, 200)
t.penup()
t.goto(0, 50)
t.pendown()
t.write("All About Me", font=("arial", 30, "bold"), align="center")
t.penup()
t.goto(0, -50)
t.pendown()
t.write("Evie Dillon", font=("arial", 30, "bold"), align="center")
enter = input("press enter to begin")
t.showturtle()
t.clear()


t.penup()
t.goto(0,250)
t.write("My favorite food", font=("arial", 30, "bold"), align="center")


turtle.addshape("sushi.gif")
t.shape("sushi.gif")
t.goto(150,150)
a = t.stamp()
t.hideturtle()
turtle.addshape("sushi2.gif")
t.shape("sushi2.gif")
t.goto(200,200)
a = t.stamp()
t.hideturtle()
t.goto(150,200)
t.write("Sushi", font=("arial", 30, "bold"), align="center")


turtle.addshape("pizza.gif")
t.shape("pizza.gif")
t.goto(0,0)
b = t.stamp()
t.goto(0,50)
t.write("Pizza", font=("arial", 30, "bold"), align="center")


turtle.addshape("applepie.gif")
t.shape("applepie.gif")
t.goto(-150,-150)
turtle.addshape("applepie2.gif")
t.shape("applepie2.gif")
t.goto(200,200)
c = t.stamp()
t.goto(0,0)
t.goto(-150,-100)
t.write("Apple pie", font=("arial", 30, "bold"), align="center")
enter = input("press enter to begin")
t.clear()
t.clearstamps()
t.penup()
t.goto(0,200)
t.write("My favorite hobbies", font=("arial", 30, "bold"), align="center")


t.goto(150,50)
t.write("Crochet", font=("arial", 30, "bold"), align="center")
turtle.addshape("crochet.gif")
t.shape("crochet.gif")
t.goto(150,150)
turtle.addshape("crochet2.gif")
t.shape("crochet2.gif")
t.goto(200,200)
d = t.stamp()
t.hideturtle()


t.goto(0,-100)
t.write("Baking", font=("arial", 30, "bold"), align="center")
turtle.addshape("baking.gif")
t.shape("baking.gif")
turtle.addshape("baking2.gif")
t.shape("baking2.gif")
t.goto(200,200)
t.goto(0,0)
e = t.stamp()


t.goto(150,-250)
t.write("Gaming", font=("arial", 30, "bold"), align="center")
turtle.addshape("gaming.gif")
t.shape("gaming.gif")
turtle.addshape("gaming2.gif")
t.shape("gaming2.gif")
t.goto(200,200)
t.goto(150,-150)
f = t.stamp()
t.goto(0,0)


t.goto(-150,50)
t.write("Writing", font=("arial", 30, "bold"), align="center")
turtle.addshape("writing.gif")
t.shape("writing.gif")
turtle.addshape("writing2.gif")
t.shape("writing2.gif")
t.goto(200,200)
t.goto(-150,150)
g = t.stamp()
t.goto(0,0)
t.clear()
t.clearstamps()
t.penup()
t.goto(0,200)
t.write("My favorite movie", font=("arial", 30, "bold"), align="center")


t.goto(150,50)
t.write("Scott Pilgrim VS the World", font=("arial", 30, "bold"), align="center")
turtle.addshape("spvtw.gif")
t.shape("spvtw.gif")
turtle.addshape("spvtw2.gif")
t.shape("spvtw2.gif")
t.goto(200,200)
t.goto(150,150)
d = t.stamp()
t.hideturtle()
t.clear()
t.clearstamps()
t.penup()
t.goto(0,200)
t.write("My favorite sport", font=("arial", 30, "bold"), align="center")


t.goto(150,50)
t.write("Hockey", font=("arial", 30, "bold"), align="center")
turtle.addshape("hockey.gif")
t.shape("hockey.gif")
turtle.addshape("hockey2.gif")
t.shape("hockey2.gif")
t.goto(200,200)
t.goto(150,150)
d = t.stamp()
t.hideturtle()




enter = input("press enter to continue")
t.clear()
t.clearstamps()


turtle.done()
