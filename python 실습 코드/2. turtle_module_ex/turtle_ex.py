import turtle

def draw_circle(bongwon):
    bongwon.circle(50)

def draw_star(bongwon):
    for _ in range(5):
        #별은 5개의 꼭지점이 있으므로 360 / 5 * 2한 값만큼 오른쪽으로 돈다.
        bongwon.right(360 / 5 * 2)
        #별을 그릴것이므로 우선 원의 지름만큼 이동한다.
        bongwon.forward(100)

def draw_square(bongwon):
    for i in range(1, 5):
        if i == 3:
            #네모의 중간에서 원과 별을 그리기 위한 준비를 마친다.
            bongwon.forward(50)
            draw_circle(bongwon)
            draw_star(bongwon)
            bongwon.forward(50)
        else:
            bongwon.forward(100)
        bongwon.right(90)

def draw_my_art():
    window = turtle.Screen()
    window.bgcolor('red')

    bongwon = turtle.Turtle()
    bongwon.shape("turtle")
    bongwon.color("blue")
    bongwon.speed(3)

    for i in range(1, 40):
        draw_square(bongwon)
        bongwon.right(10)
    
    window.exitonclick()

draw_my_art()
