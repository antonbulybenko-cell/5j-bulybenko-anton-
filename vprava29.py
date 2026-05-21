from turtle import *

Screen().setup(1.0, 1.0)
delay(600)

speed(0)

color('blue')
for i in range(1, 100, 1):
  up()
  goto(i*2, i*1.5)
  down()
  circle(i)


done()
  
