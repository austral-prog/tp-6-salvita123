def remove_elements(lst):
    indices = [0, 4, 5]
    return [item for i, item in enumerate(lst) if i not in indices]

sample1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("remove_elements:", remove_elements(sample1))


def add_elements(lst):
    return ['Pink'] + lst + ['Yellow']

sample2 = ['Red', 'Green', 'White', 'Black']
print("add_elements:", add_elements(sample2))


def is_empty(lst):
    return len(lst) == 0

print("is_empty (lista vacía):", is_empty([]))
print("is_empty (lista con elementos):", is_empty(['a']))


def check_lists(lst1, lst2):
    if len(lst1) > 2 and len(lst2) > 2:
        return lst1[2] == lst2[2]
    return False

list1a = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
list2a = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
print("check_lists (True):", check_lists(list1a, list2a))

list1b = ['Black', 'Pink', 'Green', 'White']
list2b = ['Red', 'Green', 'Yellow', 'Black', 'Pink']
print("check_lists (False):", check_lists(list1b, list2b))


def list_of_lists(big_list):
    result = []
    if len(big_list) >= 1:
        result.append(big_list[0][:2])
    if len(big_list) >= 2:
        result.append(big_list[1][1:4])
    if len(big_list) >= 3:
        result.append(big_list[2][-2:])
    return result

sample3 = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
print("list_of_lists:", list_of_lists(sample3))  

