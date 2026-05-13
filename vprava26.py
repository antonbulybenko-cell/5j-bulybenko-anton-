from random import*

a = randint(1, 20)
print('a =', a) 
b = randint(1, 20)
print('b =', b) 

x = a>b
print('a > b =', x)

y = b<=10
print('b <= 10 =', y)

print('x and y =', x and y)
print('x or y =', x or y)
print('not x and y =', not x and y)
print('not(x and y) =', not(x and y))
