import unittest
from example2 import *

class GenEx2Tests(unittest.TestCase):
    "Unittest setup file. Unitetst framework will run this before every test."
    def setUp(self):
        pass
    
    #---Test get_positives ----------------------------------
    def test_get_positives(self):
        self.assertEqual(get_positives([1, 0, -2, -1, 2,-3, 3]), [1,2,3])

    #---Test get_evens ----------------------------------
    def test_get_evens(self):
        self.assertEqual(get_evens([1,2,3,4,5,6]), [2,4,6])

    #---Test get_longer ----------------------------------
    def test_get_longer(self):
        self.assertEqual(get_longer(['Python','IS','so', 'much','FUn'], 4), ['Python','much'])

   
if __name__ == '__main__':
    unittest.main()

