floors = int(input())
units_per_floor = int(input())

units_count = floors * units_per_floor

for i in range(floors, 0, -1):
    if i == floors:
        for j in range(units_per_floor):
            print(f'L{i}{j}', end=' ')
    elif i % 2 != 0:
        for j in range(units_per_floor):
            print(f'A{i}{j}', end=' ')
    elif i % 2 == 0:
        for j in range(units_per_floor):
            print(f'O{i}{j}', end=' ')
    
    print()