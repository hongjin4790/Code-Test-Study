n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
result = 0
if k < n:
    sensor.sort()
    c = []
    for i in range(1, n):
        c.append(sensor[i]-sensor[i-1])
    c.sort()
    for j in range(k-1):
        c.pop()

    for q in range(0,len(c)):
        result += c[q]
print(result)
