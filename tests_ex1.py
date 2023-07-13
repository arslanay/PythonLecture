import unittest
from example1 import *

class GenEx1Tests(unittest.TestCase):
    "Unittest setup file. Unitetst framework will run this before every test."
    def setUp(self):
        pass
    
    #---Test add_to_all ----------------------------------
    def test_add_to_all(self):
        self.assertEqual(add_to_all([1,2,3],10), [11,12,13])
 
    #---Test lower_all ----------------------------------
    def test_lower_all(self):
        self.assertEqual(lower_all(['Python','IS','FUn']), ['python','is','fun'])

    #---Test length_of_all ----------------------------------
    def test_length_of_all(self):
        self.assertEqual(length_of_all(['Python','IS','FUn']), [6,2,3])

   
if __name__ == '__main__':
    unittest.main()

