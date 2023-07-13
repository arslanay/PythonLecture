"Generalization of processes - example3"

def sum_list(lst):
    """Sums all values in a list. 
    >>> sum_list([1, 0, 4, -2, -1, 2,-3, 3, 2])
    6  
    """
    if len(lst) == 0:
        return None
    base = lst[0]
    for item in lst[1:]:
        base += item
    return base

sum_output = sum_list([1, 0, 4, -2, -1, 2,-3, 3, 2])
assert (sum_output == 6),f"expected 6 , got {sum_output}"

##-------------------------------------------------

def max_of_list (lst):
    """Returns the maximum value from list 'lst'. 
    >>> max_of_list([1, 0, 4, -2, -1, 2,-3, 3, 2])
    4  
    """
    if len(lst) == 0:
        return None
    base = lst[0]
    for item in lst[1:]:
        base = max(base,item)
    return base

max_output = max_of_list([1, 0, 4, -2, -1, 2,-3, 3, 2])
assert (max_output == 4),f"expected 4 , got {max_output}"

##-------------------------------------------------

def longest(lst):
    """Returns the longest (leftmost) value from list 'lst'. 
    >>> longest(['Python','is','so','much','fun'])
    'Python'  
    """
    def longer(l1,l2):
        """Returns the longer of the two given lists. """
        if len(l1)>len(l2):
            return l1
        else:
            return l2

    if len(lst) == 0:
        return None
    base = lst[0]
    for item in lst[1:]:
        base = longer(base,item)
    return base

longest_output = longest(['Python','is','so','much','fun'])
assert (longest_output == 'Python'),f"expected 'Python', got {longest_output}"

##-------------------------------------------------