def recursive_binary_search(data, target,  low, high):
    """[binary search using recursion, works with a sorted list]

    Args:
        data ([list]): [sorted list ]
        target ([any]): [element we need to find in data]
        low ([interger]): [starting point of our search]
        high ([interger]): [ending point of our search]

    Returns:
        [bool]: [True if the target is in data else False]
    """ 
    if low > high:
        return False
    else:
        mid = (high + low) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return recursive_binary_search(data, target, low, mid - 1)
        else:
            return recursive_binary_search(data, target, mid + 1, high)