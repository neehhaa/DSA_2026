"""
*
**
***
****
*****
"""

lines = int(input("Enter number of lines: "))

for outer in range (lines):
    for inner in range (outer+1):
        print("*", end="")
    print()
