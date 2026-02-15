num = int(input())

def print_n(n):
    if n ==0:
        return
    print(n)
    n -=1
    print_n(n)

print_n(num)