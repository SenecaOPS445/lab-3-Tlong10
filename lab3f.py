#!/usr/bin/env python3

# Place my_list below this comment (before the function definitions)

my_list = [ 1, 2, 3, 4, 5 ]

def add_item_to_list(ordered_list):
    new = my_list[-1] + 1
    my_list.append(new)
    # Appends new item to end of list with the value (last item + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    for value in items_to_remove:
        ordered_list.remove(value)

    # Removes all values, found in items_to_remove list, from ordered_list

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)
