import turtle
end=150
over=turtle.Turtle()
over.color("white")
turtle.tracer(0)
screen=turtle.Screen()
screen.title("ROCKET MAZE GAME ")
screen.bgpic("bg.gif")
rt=turtle.Turtle()
screen.addshape("rocketup.gif")
screen.addshape("rocketdn.gif")
screen.addshape("rocketlt.gif")
screen.addshape("rocketrt.gif")
screen.addshape("man.gif")
screen.addshape("thank.gif")
rt.shape("rocketup.gif")
rt.penup()
rt.goto(180,-250)
man=turtle.Turtle()
man.shape("man.gif")
man.penup()
man.goto(-110,270)
line=turtle.Turtle()
line.color("brown")
line.pensize(10)
def loop(ran,x,y,hd):
    line.penup()
    for i in range(ran):
        line.goto(x,y)
        line.setheading(hd)
        line.pendown()
        line.fd(i)
        out()

def restart_game():

    rt.goto(180, -250)    
    screen.bgpic("bg.gif")    
    screen.onkeypress(up,"Up")
    screen.onkeypress(down,"Down")
    screen.onkeypress(right,"Right")
    screen.onkeypress(left,"Left")   
    screen.listen()
    game()
    
    
def out():
    line.clear()
    if rt.distance(line)<10 or i==end:
            screen.bgpic("LOSE.gif")
            over.clear()
            screen.onkeypress(None, "Up")
            screen.onkeypress(None, "Down")
            screen.onkeypress(None, "Right")
            screen.onkeypress(None, "Left")
            screen.onkeypress(restart_game, "Return")
            screen.onkeypress(screen.bye,"Escape")

def up():
    rt.shape("rocketup.gif")
    rt.setheading(90)
    rt.fd(10)


def down():
    rt.shape("rocketdn.gif")
    rt.setheading(270)
    rt.fd(10)

def right():
    rt.shape("rocketrt.gif")
    rt.setheading(0)
    rt.fd(10)

def left():
    rt.shape("rocketlt.gif")
    rt.setheading(180)
    rt.fd(10)

screen.onkeypress(up,"Up")
screen.onkeypress(down,"Down")
screen.onkeypress(right,"Right")
screen.onkeypress(left,"Left")
screen.listen()
def game():
        
    global i
    i=0
    while i<=end:
        over.hideturtle()
        over.clear()
        over.penup()
        over.goto(0,255)
        over.pendown()
        over.write(end-i,font=("ariel",24))
        

        line.hideturtle()
        if man.distance(rt)<50:
            screen.bgpic("thank.gif")
            over.clear()
            screen.onkeypress(None, "Up")
            screen.onkeypress(None, "Down")
            screen.onkeypress(None, "Right")
            screen.onkeypress(None, "Left")
            screen.onkeypress(restart_game, "Return")
            screen.onkeypress(screen.bye,"Escape")
        loop(60,-130,-250,90)
        loop(70,-125,-200,180)
        loop(60,-75,-200,90)
        loop(60,-75,-140,0)
        loop(60,-20,-140,90)
        loop(280,-130,-255,0)
        loop(60,153,-255,90)
        loop(170,150,-195,180)
        loop(60,208,-195,270)
        loop(170,208,-140,180)
        loop(60,38,-140,90)
        loop(120,38,-85,0)
        loop(60,152,-85,90)
        loop(60,152,-27,0)
        loop(60,210,-27,90)
        loop(60,205,30,0)
        loop(60,265,-85,180)
        loop(170,153,255,270)
        loop(60,153,85,0)
        loop(110,210,85,90)
        loop(110,-75,255,270)
        loop(60,-75,143,180)
        loop(5,-15,143,0)
        loop(60,-17,143,90)
        loop(110,-17,200,0)
        loop(60,-130,255,270)
        loop(170,-185,200,270)
        loop(280,-130,-255,0)
        loop(60,-185,30,180)
        loop(60,-245,-85,0)
        loop(115,-245,-140,0)
        loop(170,-130,-140,90)
        loop(60,-130,-28,180)
        loop(60,-130,-85,0)
        loop(170,-73,-85,90)
        loop(60,-73,85,180)
        loop(110,-73,85,0)
        loop(60,40,85,270)
        loop(60,40,143,0)
        loop(170,95,143,270)
        loop(170,95,-27,180)
        loop(60,-17,-27,90)
        loop(60,95,27,0)
        i+=1
        turtle.update()
        
    out()
game()
turtle.done()
