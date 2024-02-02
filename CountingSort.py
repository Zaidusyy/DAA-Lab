def countingSort(arr):
    size = len(arr)
    output = [0] * size

    max_val = max(arr)
    

    count = [0] * (max_val + 1)

    for i in range(0, size):
        count[arr[i]] += 1

    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]


n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter Element : "))
    arr.append(num)

print(arr)
countingSort(arr)
print(arr)
