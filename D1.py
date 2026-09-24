def fun1(x):
    return x**3 - x - 1

def fun2(x):
    return 3 * x**2 - 1

eps = 0.000001
x0 = 1.5
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
n = 0
while (b - a) > eps:
    c = (a + b) / 2
    n += 1
    if fun1(a) * fun1(c) < 0:
        b = c
    else:
        a = c
res = (a + b) / 2

n2 = 0
while True:
    x1 = x0 - fun1(x0) / fun2(x0)
    n2 += 1
    if abs(x1 - x0) <= eps:
        break
    x0 = x1
res2 = x1

print()
print(f"{'Метод':<20}{'Результат':<20}{'Итераций':^10}")
print()
print(f"{'Бисекция':<20}{res:<20}{n:^10}")
print(f"{'Ньютон':<20}{res2:<20}{n2:^10}")
print()

if n > n2:
    print(f" ~ Метод Ньютона быстрее в {n / n2} раз ~ ")
elif n < n2:
    print(f" ~ Метод Бисекции быстрее в {n2 / n} раз ~ ")
else:
    print("Они одинаковы по скорости либо где то ошибка!")
