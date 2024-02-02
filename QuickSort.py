def quick_sort(nums, low, high):
    if low >= high:
        return

    s = low
    e = high
    m = s + (e - s) // 2
    pivot = nums[m]

    while s <= e:
        while nums[s] < pivot:
            s += 1
        while nums[e] > pivot:
            e -= 1

        if s <= e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1

    quick_sort(nums, low, e)
    quick_sort(nums, s, high)

if __name__ == '__main__':
    n = int(input("Enter the number of elements: "))
    arr = []
    for i in range(n):
        num = int(input("Enter Element : "))
        arr.append(num)
    print('before sort : ',arr)
    quick_sort(arr, 0, len(arr) - 1)
    print('After sort :',arr)

