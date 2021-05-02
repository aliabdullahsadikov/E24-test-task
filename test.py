import unittest
from main import MyList

class TestRevers(unittest.TestCase):

    def test_chack_digits(self):
        # Valid List
        revers_first = MyList([2,9,5], [4,3,7])
        result = revers_first.chack_digits()
        self.assertTrue(result, True)

        # List numbers lower from 0
        revers_second = MyList([2,-9,5], [4,3,7])
        result = revers_second.chack_digits()
        self.assertFalse(result, False)

        # List numbers upper from 9
        revers_third = MyList([2,9,55], [4,23,7])
        result = revers_third.chack_digits()
        self.assertFalse(result, False)


    def test_convert_to_integer(self):
        # Valid
        l1 = [2,6,8]
        l2 = 2
        my_list = MyList(l1, l2)
        result = my_list.convert_to_integer(my_list.list1)
        self.assertTrue(type(result), int)

        # Invalid
        result_2 = MyList.convert_to_integer(my_list.list2)
        self.assertFalse(result_2, False)


if __name__ == "__main__":
    unittest.main()