from turtle import *

width (3)
# корпус човна
fillcolor('brown')
begin_fill()
goto(-40, 50)
goto(120, 50)
goto(80, 0)
goto(0, 0)
end_fill()

up()
goto(40, 50)
# вітрила
fillcolor('red')
begin_fill()
down()
goto(40, 130)
goto(70, 95)
goto(40, 60)
end_fill()

# кит
up()
goto(250, 0)
down()
left(90)
fillcolor('LightYellow')
begin_fill()
circle(50, 180)
goto(270, 0)
goto(270, 20)
goto(250, 0)
up()
goto(180,20)
dot(15)
end_fill()

# хвилі
color('blue')
up()
goto(-10, 0)
down()
goto(-70, 0)
goto(-70, 15)
goto(-130, 15)

up()
goto(-25, 20)
down()
goto(-85, 20)
goto(-85, 35)
goto(-145, 35)

up()
goto(100, 5)
down()
goto(140, 5)

up()
goto(115, 20)
down()
goto(150, 20)

# сонце
color('orange', 'orange')
up()
goto(200, 200)
down()
begin_fill()
circle(30)
end_fill()

# промені
up()
goto(190, 220)
down()
goto(270, 180)

up()
goto(190, 180)
down()
goto(270, 220)

up()
goto(230, 240)
down()
goto(230, 160)


done()