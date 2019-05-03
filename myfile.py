import unittest 
  
class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def setup(self):
        print("setting_up")
    def test(self):         
        self.assertTrue(True) 
  
if __name__ == '__main__': 
    unittest.main() 