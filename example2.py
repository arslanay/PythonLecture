"Generalization of processes - example1"

def get_positives(lst):
    """Filters out the negative values and zero from list 'lst'. 
    >>> get_positives([1, 0, -2, -1, 2,-3, 3])
    [1,2,3]
    """
    out = []
    for item in lst:
        if item > 0:
            out.append(item)
    return out

positives_output = get_positives([1, 0, -2, -1, 2,-3, 3])
assert (positives_output == [1,2,3]),f"expected [1,2,3] , got {positives_output}"

##-------------------------------------------------

def get_evens(lst):
    """Filters out the odd values from list 'lst'.
    >>> get_evens([1,2,3,4,5,6])
    [2,4,6]
    """
    out = []
    for item in lst:
        if item % 2 == 0:
            out.append(item)
    return out

evens_output = get_evens([1,2,3,4,5,6])
assert (evens_output == [2,4,6]),f"expected [2,4,6] , got {evens_output}"

##-------------------------------------------------

def get_longer(lst, n):
    """Filters out the words shorter than 'n' characters from list 'lst'.
    >>> get_longer(['Python','IS','so', 'much','FUn'],4)
    ['Python','much']
    """
    out = []
    for item in lst:
        if len(item) >= n:
            out.append(item)
    return out

longer_output = get_longer(['Python','IS','so', 'much','FUn'], 4)
assert (longer_output == ['Python','much']),f"expected ['Python','much'] , got {longer_output}"

##-------------------------------------------------