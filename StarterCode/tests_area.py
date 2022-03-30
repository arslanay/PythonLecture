import unittest
from area import *

class AreaTests(unittest.TestCase):
    "Unittest setup file. Unitetst framework will run this before every test."
    def setUp(self):
        pass
    
    #---Test area_of_square ----------------------------------
    def test_area_of_square(self):
        self.assertEqual(area_of_square(4),16)

    #---Test area_of_circle ----------------------------------
    def test_area_of_circle(self):
        self.assertAlmostEqual(area_of_circle(4),50.2655,4)

    #---Test area_of_sphere ----------------------------------
    def test_area_of_sphere(self):
        self.assertAlmostEqual(area_of_sphere(4),201.0619,4)

   
if __name__ == '__main__':
    unittest.main()

