import turtle
colors = ['orange','red','blue','yellow','green']
screen = turtle.Screen()
trl = turtle.Turtle()
trl.speed(-1)
screen.bgcolor('black')
for x in range(360):
    trl.pencolor(colors[x % 5])
    trl.width(x/5+1)
    trl.backward(x)
    trl.left(25)