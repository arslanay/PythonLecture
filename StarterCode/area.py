"Generalization example"

from math import pi

def area_of_square (r):
    """Calculates the area of a square.
    """
    assert r>0, "Length should be positive!"
    return r*r

def area_of_circle (r):
    """Calculates the area of a circle.
    """
    assert r>0, "Length should be positive!"
    return pi*r*r

def area_of_sphere (r):
    """Calculates the area of a sphere.
    """
    assert r>0, "Length should be positive!"
    return 4*pi*r*r