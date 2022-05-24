n = int(input())
combinations_count = 0

for x in range(0, n + 1):
    for y in range(0, n + 1):
        for z in range(0, n + 1):
            if x + y + z == n:
                combinations_count += 1

print(combinations_count)
