#bowling tests
import unittest
from bowling import calc
class BowlingTests(unittest.TestCase):
    #Tests for bowling.py
    
    def test_strikes(self):
        #Tests all strikes
        score1 = calc(["X","X","X","X","X","X","X","X","X","X","X","X"])
        score2 = calc(["2","3","2","3","2","3","2","3","2","3","2","3","2","4","2","3","4","2","4","/","9"]) 
        score3 = calc(["6","/","X","4","5","X","X","3","/","X","3","4","9","-","X","3","/"]) 
        score4 = calc(["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]) 
        
        self.assertEqual(score1, 300)
        self.assertEqual(score2, 66)
        self.assertEqual(score3, 164)
        self.assertEqual(score4, 0)
        
if __name__ == "__main__":
    unittest.main()