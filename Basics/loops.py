for i in range(5):
    print(f'{i} ', end="")
print(" ")
for i in range(4, 10):
    print(f'{i} ', end="")
print(" ")
x = 3
while x < 10:
    print(x, end=" ")
    x = x + 1
    if x == 5:
        break
print(" ")
a = ['a', 'b', 'c', 5, [1, 2]]
for i in a:
    print(f'{i} {type(i)}')
for i, l in enumerate(a, start=0):
    print(f'{i} {l}')

