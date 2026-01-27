lines = int(input("Enter the number of lines: "))
for rows in range(0, lines):
    for columns in range(0,lines):
        print(columns+1,end=' ')
    lines = lines -1
    print()