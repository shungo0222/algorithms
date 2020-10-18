# O(n)

def linear_search(key, target_list):
    index = 0
    target_list.append(key)     # Sentinel
    while target_list[index] != key:
        index += 1
    if index == len(target_list) - 1:
        return -1     # Not found
    return index

x = [1, 3, 4, 7, 12, 72, 80, 2]
print(linear_search(7, x))