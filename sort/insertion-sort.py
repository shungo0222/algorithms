# stable sort
# O(n**2)


def insertion_sort(array):
    for i in range(1, len(array)):
        tmp = array[i]
        j = i - 1
        while array[j] > tmp and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = tmp
    return array


x = [32, 11, 8, 34, 79, 100, 43, 52, 69]
print(x)
print(insertion_sort(x))