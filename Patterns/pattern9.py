"""
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
"""

lines = int(input("Enter number of lines: "))
for rows in range (0, lines):
    for space in range (0, lines-rows-1):
        print(" ", end="")
    for star in range (0,2*rows+1):
        print("*", end="")
    for space in range (0, lines-rows-1):
        print(" ", end="")
    print()
for rows in range (0, lines):
    for space in range (0, rows):
        print(" ", end="")
    for star in range (0,2*(lines-rows)-1 ):
        print("*", end="")
    for space in range (0, rows):
        print(" ", end="")
    print()
