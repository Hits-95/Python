import turtle
my_an = turtle.Screen()
my_an.speed(2)
my_an.turtle.width(5)
for i in range(30):
    my_an.circle(30)
    my_an.circle(5*i)
    my_an.circle(-5*i)
    my_an.left(i)
my_an.exitonclick()
