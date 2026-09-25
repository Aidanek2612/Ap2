import math

def phi (x):
    return math.cos(x)

def phi1 (x):
    return -math.sin(x)

x0 = 1
eps = 0.000001
x1 = phi (x0)
res = abs(x1-x0)


print("ffff")
print (f"Начальное приближение x0 = {x0}")
print (f"x1 = {x1}")
print (f"Разница = {res}")

