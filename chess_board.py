import turtle
def db(t,x,y,size,fill):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(fill)
    t.begin_fill()
    for i in range(0,4):
        board.fd(size)
        board.rt(90)

    t.end_fill()

def dcb():
    sq_color="black"
    x=y=0
    box_size=30
    for i in range(0,8):
        for j in range(0,8):
            db(board,x+j*box_size,y+i*box_size,box_size,sq_color)
            if sq_color=="white":
                 sq_color="black"
            else: sq_color="white"
        if sq_color=="white":
             sq_color="black"
        else: sq_color="white"

board=turtle.Turtle()
dcb()
