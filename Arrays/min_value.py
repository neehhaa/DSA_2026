values = [3,5,1,6,3,4,7,8,9,4,-1]
min_value=values[0]
for index in  values:
    if index < min_value:
        min_value = index

print(min_value)
