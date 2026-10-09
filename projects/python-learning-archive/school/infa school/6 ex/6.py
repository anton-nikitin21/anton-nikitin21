from turtle import*
tracer(0)
screensize(5000,5000)
r=30

# xcor() текущие координаты черепахи
# ycor() 

for i in range(2):
    goto(xcor()+3*r,ycor()+4*r)
    goto(xcor()-3*r,ycor()+4*r)
    goto(xcor()-3*r,ycor()-4*r)
    goto(xcor()+3*r,ycor()-4*r)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(4,'red')
update()
mainloop()