def merinplace(arr, s, e):
    if s < e:
        mid = (s + e) // 2
        merinplace(arr, s, mid)
        merinplace(arr, mid + 1, e)
        merge(arr, s, e, mid)

def merge(arr, s, e, m):
    i = s
    j = m + 1
    k = 0
    mix = []

    while i <= m and j <= e:
        if arr[i] <= arr[j]:
            mix.append(arr[i])
            i += 1
        else:
            mix.append(arr[j])
            j += 1
        k += 1

    while i <= m:
        mix.append(arr[i])
        i += 1
        k += 1

    while j <= e:
        mix.append(arr[j])
        j += 1
        k += 1

    for l in range(len(mix)):
        arr[s + l] = mix[l]

if __name__ == '__main__':
    n = int(input("Enter the number of elements: "))
    arr = []
    for i in range(n):
        num = int(input("Enter Element : "))
        arr.append(num)

    print(arr)
    merinplace(arr, 0, len(arr) - 1)
    print(arr)

