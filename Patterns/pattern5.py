"""
*****
****
***
**
*
"""

lines = int(input("Enter number of lines: "))

for outer in range (0, lines):
    for inner in range (0, lines-outer):
        print("*", end="")
    print()
