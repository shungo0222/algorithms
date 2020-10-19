# O(log(n))

def binary_search(key, target_list):
    left = 0
    right = len(target_list)
    while left < right:
        mid = (left + right) // 2
        if target_list[mid] == key:
            return mid
        elif key < target_list[mid]:
            right = mid
        else:
            left = mid + 1
    return -1     # Not found

x = [12, 3, 8, 19, 71, 31, 22, 17, 20, 4, 100]
x.sort()
print(x)
print(binary_search(8, x))