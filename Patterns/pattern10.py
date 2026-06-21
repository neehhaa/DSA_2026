"""
*
**
***
****
*****
****
***
**
*
"""

lines = int(input("Enter number of lines: "))
for rows in range (0, 2*lines-1):
    stars= rows+1
    if rows> lines-1:
        stars= 2*lines-rows-1
    for columns in range(0,stars):
        print("*", end='')
    print()
