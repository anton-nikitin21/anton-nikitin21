from turtle import*

tracer(0)
screensize(5000,5000)

r=15

for i in range(8):
    fd(16*r)
    rt(90)
    fd(22*r)
    rt(90)

up()
fd(5*r)
rt(90)
fd(5*r)
lt(90)
down()
for i in range(8):
    fd(52*r)
    rt(90)
    fd(77*r)
    rt(90)
up()    
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(4,'red')
        
update()
mainloop()
