# turtle의 onkey와 ontimer 메서드를 이용하여 's' 키를 누르면 9에서 카운트 다운이 시작되어 0에 도달하면 폭파되는 시한 폭탄을 만든다. 
# 그 외에 사항은 다음을 따른다.

#- 화면의 크기는 400x400이고 폰트 크기는 150으로 한다.
#- 처음에 화면은 초록색으로 하고  write 메서드로 "준비!"라고 표시한다.
#- 카운트 다운에서 남은 시간을 초로 표시한다.
#- 폭파할 때 화면은 빨간색이고 "쾅!!"이라고 표시한다.
#- 폭파 후 'space' 키를 누르면 다시 초기 화면으로 돌아간다.

import turtle

def move(x, y):
    # pen up
    tu.pu() 
    tu.goto(x, y)
    tu.pd()
def explode():
    tu.clear()
    screen.bgcolor('red')
    move(-150, -100)
    tu.write('쾅!!', font=('맑은 고딕', 150, 'bold'))
def countDown():
    global count
    tu.clear()
    screen.bgcolor('orange')
    move(-70, -100)
    tu.write(count, font=('맑은 고딕', 150, 'bold'))
    count -= 1
    if count >= 0:
        screen.ontimer(countDown, 1000)
    else:
        explode()
def renew():
    global count
    tu.clear()
    screen.bgcolor('green')
    count = 9

screen = turtle.Screen()
screen.setup(400, 400)
tu = turtle.Turtle()
count = 9

screen.onkey(renew, 'space')
screen.onkey(countDown, 's')
screen.listen()
screen.mainloop()