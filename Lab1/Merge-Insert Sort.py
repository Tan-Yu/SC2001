s = 5
num = 0

def merge(array, m, n):
    global num
    mid = int((m+n)/2)
    a = m
    b = mid + 1
    if n-m <= 0:
        return
    while a <= mid and b <= n:
        # print(array)
        # print("m = " + str(m))
        # print("n = " + str(n))
        print(num)
        num += 1

        print((array[a], array[b]))
        if array[a] > array[b]:
            tmp = array[b]
            b += 1
            mid += 1
            for i in range(mid, a, -1):
                array[i] = array[i-1]
            array[a] = tmp
            a += 1
        elif array[a] < array[b]:
            a += 1
        else:
            if a == mid and b == n:
                break
            tmp = array[b]
            b += 1
            a += 1
            mid += 1
            for i in range(mid, a, -1):
                array[i] = array[i-1]
            array[a] = tmp
            a += 1

def merge_insert_sort(array, m, n):
    mid = int((m + n) / 2)
    if n-m <= 0:
        return

    if mid - m + 1 <= s:
        insertion_sort(array, m, mid)
    else:
        merge_insert_sort(array, m, mid)

    if n - mid + 2 <= s:
        insertion_sort(array, mid+1, n)
    else:
        merge_insert_sort(array, mid+1, n)

    merge(array, m, n)

def mergesort(array, m, n):
    mid = int((m + n) / 2)
    if n - m <= 0:
        return
    elif n - m > 1:
        mergesort(array, m, mid)
        mergesort(array, mid + 1, n)
    merge(array, m, n)


def swap(array, j, i):
    k = array[j]
    array[j] = array[i]
    array[i] = k


def insertion_sort(array, m, n):
    global num
    for i in range(m+1, n+1):
        for j in range(i, m, -1):
            num += 1
            print(num)
            print((array[j-1], array[j]))
            if array[j] < array[j-1]:
                swap(array, j, j-1)
            else:
                break
        # print(array)

x = [1, 5, 10, 9, 6, 29, 20, -1, 0, 15, 32, 29]
y = [20, -1, 0, 15, 32, 29]
z = []

def helper(array):
    mergesort(array, 0, len(array) - 1)
    print(array)
    print(num)

helper(x)
