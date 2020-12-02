def binary_Search_iterative1(data, target):
    """[Searches in an array using divide and conquer method intereatively]
    Args:
        data (list): [len() > 0]
        target (any): [targeted value in data]

    Returns:
        [bool]: [True if target is founf else Fasle]"""  
    low = 0
    high = len(data) 
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            high = mid  
        else:
            low = mid
    return False]

