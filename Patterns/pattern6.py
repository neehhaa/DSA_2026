"""
12345
1234
123
12
1
"""

lines = int(input("Enter number of lines: "))

for outer in range (0, lines):
    for inner in range (0, lines-outer):
        print(inner+1, end="")
    print()
