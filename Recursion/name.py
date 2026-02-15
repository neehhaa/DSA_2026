num = int(input("Enter the number of times name should be printed: "))
counter = 0
def print_name(n,count):
    if count == n:
        return
    print("Neha")
    count += 1
    print_name(n,count)

print_name(num,counter)