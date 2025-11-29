def partition(array, low, high):
    pivot = array[low]
    i = low + 1
    j = high

    while True:
        while i <= j and array[i] <= pivot:
            i += 1

        while j >= i and array[j] > pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            break

    array[low], array[j] = array[j], array[low]
    return j


def quick_sort(array, low, high):
    if low < high:
        index = partition(array, low, high)
        quick_sort(array, low, index - 1)
        quick_sort(array, index + 1, high)


def print_arr(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


arr1 = [17, 60, -6, 10, 34, 22, 19, 56, 45, 29]
print("Array before Quick Sort")
print_arr(arr1, len(arr1))
quick_sort(arr1, 0, len(arr1) - 1)
print("Array after Quick Sort")
print_arr(arr1, len(arr1))