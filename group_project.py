a,b,c = int(input()),int(input()),int(input())

minimum = min(a, b, c)
maximum = max(a, b, c)
middle = a + b + c - minimum - maximum

print(maximum, middle, minimum)
