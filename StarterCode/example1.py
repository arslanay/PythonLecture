"Generalization of processes - example1"

def add_to_all (lst, val):
    """Adds 'val' to each numeric value in list 'lst'. 
       Does not change the 'lst' argument, returns a copy of the modified list. 
    >>> add_to_all([1,2,3],10)
    [11,12,13]
    """
    out = []
    for item in lst:
        out.append(item + val)
    return out

def multiply_all (lst, val):
    """Multiplies each numeric value in list 'lst' by 'val'. 
       Does not change the 'lst' argument, returns a copy of the modified list. 
    >>> multiply_all([1,2,3], 10)
    [10,20,30]
    """
    out = []
    for item in lst:
        out.append(item * val)
    return out

def lower_all (lst):
    """Converts each string in list 'lst' to lowercase. 
       Does not change the 'lst' argument, returns a copy of the modified list. 
    >>> lower_all(['Python','IS','FUn'])
    ['python','is','fun']
    """
    out = []
    for item in lst:
        out.append(item.lower())
    return out

def length_of_all (lst):
    """Calculates the length of each string in list 'lst', and returns all lengths as a list. 
       Does not change the 'lst' argument, returns a copy of the modified list. 
    >>> length_of_all(['Python','IS','FUn'])
    [6,2,3]
    """
    out = []
    for item in lst:
        out.append(len(item))
    return out