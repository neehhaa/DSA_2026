n = 3
balloons = list(map(int, input().split(' ')))
cost = 0
for i in range(1, n+1):
    print(i)
    print(balloons[i-1])
    cost += balloons[i-1] * i

print(cost)