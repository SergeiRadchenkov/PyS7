def on_update(**kwargs):
    return kwargs['a'] + kwargs['b']

a = 1
b = 2

my_sum = on_update(b=1, a=2)

print(my_sum)

print(type(on_update))

new_on_update = lambda a, b: a + b

print(new_on_update(a, b))

c = [1, 2, 2, 2, 3, 3]

print(max(c, key=c.count))