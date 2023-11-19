# Возведение числа в степень

def calk_power(degree):
    def power(num):
        return num ** degree
    return power

print(calk_power(3) (2))

# Вариант 2

cube = calk_power(3)
square = calk_power(2)

print(cube(4))
print(square(9))

# Вариант с lambda

calk_pow = lambda x, y: x**y
print(calk_pow(2, 3))

calculator = { "+": lambda x, y: x + y,
               "-": lambda x, y: x - y,
               "/": lambda x, y: x / y,
               "*": lambda x, y: x * y
            }
s = input("Введите арифметическое выражение: ")
x, op, y = s.split()
print(calculator[op](int(x), int(y)))

# Функция map

sp = [1, 2, 3, 4, 5, 6, 7]
print(*map(lambda x: x**2, sp))
print(list(map(lambda x: x**2, sp)))
print(sp2 := list(map(lambda x: x**2, sp)))

# Функция filter

print(*filter(lambda x: x % 2, sp))

# Функция enumerate

for item in enumerate(sp):
    print(item)

# Функция zip

sp2 = ['Ваня', "Вася"]
print(*zip(sp, sp2))