def reverse(i,arr,n):
    if i >= n/2:
        return
    arr[i], arr[n-1-i] = arr[n-i-1], arr[i]
    reverse(i+1,arr,n-i)
    return arr


lis = [5,4,9,8,6]

print(reverse(0,lis,len(lis)))