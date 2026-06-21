"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""
start = 1
lines = int(input("Enter number of lines: "))
for rows in range (0, lines):
    if rows % 2 == 0:
        start = 1
    for columns in range(0,rows+1):
        print(start, end=' ')
        start = 1 - start
    print()
