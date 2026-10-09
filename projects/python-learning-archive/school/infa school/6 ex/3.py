from turtle import*

tracer(0)
screensize(5000,5000)
r=30

for i in range(3):
    fd(5*r)
    lt(270)
    fd(9*r)
    rt(90)

lt(315)

for i in range(4):
    fd(11*r)
    rt(90)
    fd(5*r)
    lt(270)
    
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(4,'red')

update()
mainloop()