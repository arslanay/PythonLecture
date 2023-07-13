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

add_output = add_to_all([1,2,3],10)
assert (add_output == [11,12,13]),f"expected [11,12,13] , got {add_output}"

##-------------------------------------------------

def lower_all (lst):
    """Converts each string in list 'lst' to lowercase. 
       Does not change the 'lst' argument, returns a copy of the modified list. 
    >>> lower_all(['Python','IS','FUn'])
    ['python','is','fun']
    """
    out = []
    for item in lst:
        out.append(str.lower(item))
    return out

lower_output = lower_all(['Python','IS','FUn'])
assert (lower_output == ['python','is','fun']),f"expected ['python','is','fun'] , got {lower_output}"

##-------------------------------------------------
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

length_output = length_of_all(['Python','IS','FUn'])
assert (length_output == [6,2,3]),f"expected [6,2,3] , got {length_output}"
