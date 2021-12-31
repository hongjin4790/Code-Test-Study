# 숫자 카드 게임
result=0
n, m = map(int, input().split())
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(min_value,result)

print(result)

# 1이 될 때까지
n, k = map(int, input().split())

count = 0
while n >= k:
    if n % k == 0:
        n = n // k
        count += 1
    else:
        n -= 1
        count += 1

print(count)