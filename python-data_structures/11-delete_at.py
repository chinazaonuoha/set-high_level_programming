#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list.

    Args:
        my_list (list): The list to modify.
        idx (int): The index of the item to delete.

    Returns:
        The modified list, or the original list if the index is out of range.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
