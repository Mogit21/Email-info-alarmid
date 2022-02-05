import unittest
from okrunfunctions import queryidtable, datalisted, datatext, queryregiontable

class TestQueryTable(unittest.TestCase):

    def test_queryidtable(self):
        self.assertEqual(queryidtable("10"),[(10, 'name10', 'ipaddress10', 'office1')])
        self.assertEqual(queryidtable("99"),[(99, 'name99', 'ipaddress99', 'office10')])
        self.assertEqual(queryidtable("1,2,3"), [(1, 'name1', 'ipaddress1', 'office1'), 
                                                 (2, 'name2', 'ipaddress2', 'office1'),
                                                 (3, 'name3', 'ipaddress3', 'office1')])
        self.assertRaises(ValueError, queryidtable, "a")
    
    def test_datalisted(self):
        self.assertEqual(datalisted(queryidtable("10,15,16"),1),["name10","name15","name16"])
    
    def test_datatext(self):
        self.assertEqual(datatext(["1","2","10"]),"1,2,10")    
        
    def test_queryregiontable(self):
        self.assertEqual(queryregiontable(("office1",)), [('office1', 'region1', 'owner1')])        
    



if __name__ == '__main__':
    unittest.main()