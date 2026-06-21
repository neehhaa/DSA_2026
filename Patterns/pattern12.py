"""
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1
"""
lines = int(input("Enter number of lines: "))
for rows in range (0, lines):
    for numbers in range(0,rows+1):
        print(numbers+1, end='')
    for space in range(0, 2*(lines-rows)-2):
        print(" ", end='')
    for numbers in range(0,rows+1):
        print(rows-numbers+1, end='')
    print()
