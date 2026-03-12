arr = [13,46,24,52,20,9]
n = len(arr)
print(n)
for i in range(n):
    min_value_index = i
    for j in range(i+1,n):
        if arr[j] < arr[min_value_index]:
            min_value_index=j
    arr[i],arr[min_value_index] = arr[min_value_index],arr[i]
print(arr)