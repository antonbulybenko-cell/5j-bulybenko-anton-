from turtle import *
speed(1)

n = int(input('Введідь кількість кутів: '))

if n == 1:
  dot(10)
  circle(50)

if n == 2:
  dot(10)
  circle(50, 180)
  dot(10)
  circle(50, 180)

if n == 3:
  forward(50)
  right(120)
  forward(50)
  right(120)
  forward(50)
  right(120)

if n == 4:
  forward(50)
  right(90)
  forward(50)
  right(90)
  forward(50)
  right(90)
  forward(50)
  right(90)

if n == 5:
  forward(50)
  right(72)
  forward(50)
  right(72)
  forward(50)
  right(72)
  forward(50)
  right(72)
  forward(50)
  right(72)

if n == 6:
  forward(50)
  right(60)
  forward(50)
  right(60)
  forward(50)
  right(60)
  forward(50)
  right(60)
  forward(50)
  right(60)
  forward(50)
  right(60)

if n >= 7:
  for i in range(n):
    forward(50-n/3)
    right(360/n)
  
done()