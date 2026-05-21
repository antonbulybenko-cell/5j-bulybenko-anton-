from turtle import *
from random import *

"""
setup(400, 400)
bgcolor("darkblue")
colors = ['white', 'yellow', 'orange']
speed(0)

for i in range(1,100) :
  color(colors[i%3])
  up()
  goto (randint(-200, 200),randint(-200, 200))
  down()
  dot(randint(1,8))
"""

setup(500, 500)
colors = ['red', 'yellow', 'orange', 'green', 'blue', 'purple', 'violet']
speed(0)

for i in range(1,101) :
  color(colors[i%7], colors[i%7])
  up()
  goto (randint(-200, 200),randint(-200, 200))
  down()
  begin_fill()
  circle(randint(5,50))
  end_fill()
  

done()
  