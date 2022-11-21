import unittest
import pandas as pd
from Combiner import combineCSV
from Combiner import Diff_col_excep
from Combiner import File_not_exist



class CombineTests(unittest.TestCase):
    def test_cannot_open(self):
        self.assertRaises(File_not_exist, combineCSV, ["./fixtures/accessories.csv","./fixtures/badshi.csv"])

    def test_different_col(self):
        self.assertRaises(Diff_col_excep, combineCSV, ["./fixtures/accessories.csv","./fixtures/badTest.csv"])
        # test reutrn file_header&file_content: compare string
        # test "cannot open file exception"
      
    def test_combineCSV(self):
        # normal result testing: redirect stdout->file/string, comparing string
        # test different file columns: assertThrow
        result = pd.read_csv('combine.csv')
        test1 = pd.read_csv('standard.csv')
        self.assertTrue(test1.equals(result))



if __name__ == '__main__':
    unittest.main()