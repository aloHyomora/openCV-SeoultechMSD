# 개미 class Ant를 Trurtle에서 상속 받아 만든다. 객체를 20마리 만들어 화면에서 움직이게 한다.
# 메서드는 생성자, move, update로 하고 생성자에서는 객체의 색, 객체의 초기 위치를 인수로 받고 shape, turtlesize, color 등을 설정한다.
# move는 임의의 위치로 개미를 이동시키는 메서드이다.
# update에서는 객체를 1씩 움직이고 방향각을 randint함수로 -45에서 45 사이의 각도로  변화 시킨다. 
# 다만 각도가 너무 급격하게 변화하는 것을 막기 위하여  angle=0.7*angle+0.3*randint(-45,45) 식을 활용한다.

import turtle
import random as rnd

width, height = 500, 500

class Ant(turtle.Turtle):
    def __init__(self, col, x0, y0):
        turtle.Turtle.__init__(self) # turtle 클래스 초기화
        self.speed(0)                # 애니메이션 속도 0
        self.shape('turtle')         # 거북이 모양 (개미로 사용)
        self.color(col, 'black')     # 개미 색상 지정
        self.turtlesize(0.2)         # 크기를 작게 설정
        self.move(x0, y0)            # 초기 위치로 이동
        self.angle = 0               # 이동 각도 초기화
    def move(self, x, y):
        self.pu()
        self.goto(x, y)
        self.pd()
    def update(self):
        self.angle = 0.8 * self.angle + 0.2 * rnd.randint(-45, 45) # 기존 각도 기반으로 랜덤 값 수정
        self.left(self.angle)   # 각도 회전하기
        self.forward(1)
        
        
screen = turtle.Screen()
screen.setup(width, height)

# 20마리 개미 List로 생성
ants = [Ant((rnd.random(), rnd.random(), rnd.random()), rnd.randint(-width, width), rnd.randint(-height, height)) for _ in range(20)]
# 애니메이션 속도 최적화를 위해 화면 업데이트를 제어
screen.tracer(0)

while True:
    for ant in ants:
        ant.update()
    screen.update()