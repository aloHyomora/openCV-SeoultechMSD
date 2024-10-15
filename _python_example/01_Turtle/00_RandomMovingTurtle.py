# 무작위 이동
# 아래 그림과 같이 1000x1000의  화면에 파스텔 톤의 색상으로 자취를 남긴다.
# 직선 이동의 거리는 80, 회전 반경 20의 원을 조합하는데 회전 각도는 0, 90, 180 중 하나로 한다.

# Tip 1 : random 모듈의 random 함수를 이용하여 r, g, b 튜플로 색상을 지정한다.
# Tip 2 : turtle의 circle 함수를 이용하는데 인수는 반경과 원호의 각도이다.

import turtle
import random as rnd

# 스크린 생성, turtle 객체 생성
screen = turtle.Screen()
turtle1 = turtle.Turtle()

turtle1.width(5)
turtle1.shape('turtle')
turtle1.pencolor('red')

size = 500

# 스크린 사이즈 1000x1000
screen.setup(size, size)


# 추가 코드 (경계 설정)
min_x, max_x = -size/2, size/2
min_y, max_y = -size/2, size/2



while (True):
    # 튜플 지정 (rnd.random()) -> rgb
    col = (rnd.random()* 0.5 + 0.5, rnd.random()*0.5 + 0.5, rnd.random()*0.5 +0.5)
    turtle1.pencolor(col)
    
    angle = rnd.randint(0,2) * 90
    turtle1.circle(20, angle)
    
    turtle1.forward(80)
    x, y = turtle1.position()
    
    # 추가 코드 (화면 경계를 벗어나면 방향을 돌림)
    if x < min_x or x > max_x or y < min_y or y > max_y:
        turtle1.backward(80)  # 경계 벗어나면 다시 돌아옴
        turtle1.right(180)  # 180도 회전 후 반대 방향으로 이동