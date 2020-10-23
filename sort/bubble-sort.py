# stable sort (if "array[j] <= array[j - 1]", unstable)
# O(n**2)


def bubble_sort(array):
    n = len(array) - 1  # last index of array
    flag = True
    i = 0  # first index of unsorted part
    while flag:
        flag = False
        for j in range(n, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]  # swap
                flag = True
        i += 1
    return array


x = [32, 11, 8, 34, 79, 100, 43, 52, 69]
print(x)
print(bubble_sort(x))