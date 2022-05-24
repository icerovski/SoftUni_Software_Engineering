count = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for num in range(0, count):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 600 <= num <= 799:
        p4 += 1
    if num >= 800:
        p5 += 1

p1 = p1 / count * 100
p2 = p2 / count * 100
p3 = p3 / count * 100
p4 = p4 / count * 100
p5 = p5 / count * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')    