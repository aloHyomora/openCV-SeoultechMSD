# 5도 간격으로 5개의 원호가 연결된 꽃을 그린다. 두께를 6에서 1까지 감소시킨다.

import turtle
import random as rnd

f = lambda x : 0.5 * (x+1.)

def goHome():
    turtle1.pu()
    turtle1.goto(0, 0)
    turtle1.pd()
    
def flower(angle):
    goHome()
    turtle1.color(f(rnd.random()), f(rnd.random()), f(rnd.random()))
    turtle1.setheading(angle)
    num_segments = 5
    count = 0
    
    for k in range(num_segments):
        turtle1.width((6-count))
        radius = rnd.randrange(30, 80, 10)
        extent = rnd.randrange(30, 120, 10)
        direction = rnd.choice([1, -1])
        turtle1.circle(radius * direction, extent)        
        count += 1

screen = turtle.Screen()
screen.setup(500, 500)
turtle1 = turtle.Turtle()
turtle1.speed('fastest')
for angle in range(0, 360, 5):
    flower(angle)
    
screen.exitonclick()

