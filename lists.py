print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
# ['Green', 'White', 'Black']

print(add_elements(['Red', 'Green', 'White', 'Black']))
# ['Pink', 'Red', 'Green', 'White', 'Black', 'Yellow']

print(is_empty([]))  # True
print(is_empty(['a']))  # False

print(check_lists(['Black', 'Pink', 'Yellow'], ['Red', 'Green', 'Yellow']))  # True
print(check_lists(['Black', 'Pink'], ['Red', 'Green', 'Yellow']))  # False

print(list_of_lists([[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]))
# [[1, 2], [5, 6, 7], [11, 12]]
