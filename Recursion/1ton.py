num = int(input())

def print_n(i,n):
    if i > n:
        return
    print(i)
    i += 1
    print_n(i,n)

print_n(1,num)
