from turtle import*

tracer(0)  #отключение анимации
screensize(5000,5000)
r=10

for i in range(2):
    fd(5*r)
    rt(90)
    fd(11*r)
    rt(90)
up()
fd(-4*r)
rt(90)
fd(6*r)
lt(90)
down()
for i in range(2):
    fd(42*r)
    rt(90)
    fd(63*r)
    rt(90)

# отрисовка целочисленных 
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')


update()
mainloop()
