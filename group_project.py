# Можно использовать функцию map вместо вызывания 3 отдельных функций
a, b, c = map(int, input().split())
minimum, middle, maximum = sorted([a, b, c])


print(maximum)
print(middle)
print(minimum)
