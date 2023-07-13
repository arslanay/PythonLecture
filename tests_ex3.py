import unittest
from example3 import *

class GenEx3Tests(unittest.TestCase):
    "Unittest setup file. Unitetst framework will run this before every test."
    def setUp(self):
        pass
    
    #---Test sum_list ----------------------------------
    def test_sum_list(self):
        self.assertEqual(sum_list([1, 0, 4, -2, -1, 2,-3, 3, 2]), 6)

    #---Test max_of_list ----------------------------------
    def test_max_of_list(self):
        self.assertEqual(max_of_list([1, 0, 4, -2, -1, 2,-3, 3, 2]), 4)

    #---Test longest ----------------------------------
    def test_longest(self):
        self.assertEqual(longest(['Python','is','so','much','fun']), 'Python' )

   
if __name__ == '__main__':
    unittest.main()

