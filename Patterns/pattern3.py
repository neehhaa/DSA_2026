"""
1
12
123
1234
12345
"""

lines = int(input("Enter number of lines: "))

for outer in range (0, lines):
    for inner in range (0, outer+1):
        print(inner+1, end="")
    print()
