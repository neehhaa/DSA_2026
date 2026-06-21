"""
*********
 *******
  *****
   ***
    *
"""

lines = int(input("Enter number of lines: "))

for outer in range (0, lines):
    for inner in range (0, outer):
        print(" ", end="")
    for inner in range (0,2*(lines-outer)-1 ):
        print("*", end="")
    for inner in range (0, outer):
        print(" ", end="")
    print()
