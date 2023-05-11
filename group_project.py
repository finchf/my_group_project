a = int(input())
b = int(input())
c = int(input())

minimum = min(a, b, c)
maximum = max(a, b, c)
middle = a + b + c - minimum - maximum

print(maximum)
print(middle)
print(minimum)