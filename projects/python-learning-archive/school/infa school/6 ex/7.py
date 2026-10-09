from turtle import*
tracer(0)
screensize(5000,5000)
r=30

# xcor() текущие координаты черепахи
# ycor() 

goto(xcor(),ycor()+12*r)
goto(xcor()+5*r,ycor()-12*r)
goto(xcor()-10*r,ycor())
goto(xcor()+5*r,ycor()+12*r)
goto(xcor(),ycor()+4*r)
goto(xcor()+3*r,ycor()-4*r)
goto(xcor()-6*r,ycor())
goto(xcor()+3*r,ycor()+4*r)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(4,'red')
update()
mainloop()