lines = int(input("Enter the number of lines: "))
for rows in range (0, lines):
    for space in range(0, rows):
        print(" ",end=' ')
    for star in range((2*lines)-(2*rows) +1):
        print("*", end=' ')
    for space in range(0, rows):
        print(" ",end=' ')
    print()