# unstable sort
# O(n**2)


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        minj = i
        for j in range(i, n):
            if array[j] < array[minj]:
                minj = j
        array[i], array[minj] = array[minj], array[i]
    return array


x = [32, 11, 8, 34, 79, 100, 43, 52, 69]
print(x)
print(selection_sort(x))