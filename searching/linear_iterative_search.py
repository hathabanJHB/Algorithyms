def linear_iterative_search(data, target):
    for i in data:
        if i == target:
            return True
    return False