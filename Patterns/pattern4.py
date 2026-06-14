"""
1
22
333
4444
55555
"""

lines = int(input("Enter number of lines: "))

for outer in range (0, lines):
    for inner in range (0, outer+1):
        print(outer+1, end="")
    print()
