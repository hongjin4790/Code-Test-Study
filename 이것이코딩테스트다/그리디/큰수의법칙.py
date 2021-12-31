# 큰 수의 법칙
n, m, k = map(int,input("입력: ").split())

data = list(map(int, input().split()))
res = 0
if k <= m:
    data.sort()
    while True:
        if m == 0:
            break
        for i in range(k):
            res += data[n-1]
            m -= 1
        res += data[n - 2]
        m -= 1

print(res)