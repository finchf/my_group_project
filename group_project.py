
# Можно использовать функцию map вместо вызывания 3 отдельных функций
a, b, c = map(int, input().split())
minimum, middle, maximum = sorted([a, b, c])


print(maximum)
print(middle)
print(minimum)
=======
a, b, c = list(map(int, input('Enter three numbers, separated by spaces: ').split()))  # reading data

minimum, middle, maximum = min(a, b, c), a + b + c - min(a, b, c) - max(a, b, c), max(a, b, c)  # initialization min, mid, max
# output new data
print(f'''Minimum one: {minimum}.
Middle one: {middle}.
Maximum one: {maximum}.''')

