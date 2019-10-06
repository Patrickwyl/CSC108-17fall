import unittest
import network_functions

class TestGetFamilies(unittest.TestCase):

    def test_get_families_empty(self):
        param = {}
        actual = network_functions.get_families(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        

    def test_get_families_one_person_one_friend_diff_family(self):
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Dunphy': ['Claire']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
        
    def test_get_families_one_person_two_friends_smae_family(self):
        param = {'A Sh':['C Sh', 'B Sh']}
        actual = network_functions.get_families(param)
        expected = {'Sh': ['A', 'B', 'C']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
        
    def test_get_families_two_people_multiple_friends_diff_family(self):
        param = {'A Sh':['C Sh', 'B Sh', 'E Ck', 'D Ck'], \
                 'B Sh':['C Sh', 'D Ck']}
        actual = network_functions.get_families(param)
        expected = {'Sh': ['A', 'B', 'C'], 'Ck': ['D', 'E']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
        
    def test_get_families_two_people_multiple_first_friends_diff_family(self):
        param = {'A Sh':['C D Sh', 'B Sh', 'E Ck', 'D Ck'], \
                 'B Sh':['C D Sh', 'D Ck']}
        actual = network_functions.get_families(param)
        expected = {'Sh': ['A', 'B', 'C D'], 'Ck': ['D', 'E']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        


if __name__ == '__main__':
    unittest.main(exit=False)