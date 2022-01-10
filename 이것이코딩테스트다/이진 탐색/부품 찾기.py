def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


n = int(input())
array1 = list(map(int, input().split()))
array1.sort()
m = int(input())
array2 = list(map(int, input().split()))

for i in array2:
    result = binary_search(array1, i, 0, n-1)
    if result is None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
