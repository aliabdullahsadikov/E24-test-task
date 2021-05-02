

class MyList():

    def __init__(self, list1, list2):
        self.list1 = list1 or [0]
        self.list2 = list2 or [0]


    def chack_digits(self) -> bool:
        """
        Submitted list's numbers must be upper from 0 and lower from 9
        :return:
        """
        joinded_lists = self.list1 + self.list2
        for number in joinded_lists:
            if number < 0 or number > 9:
                return False
        return True


    def revers(self) -> str:
        """
        The digits are stored in reverse order, and each of the nodes contains a single digit.
        Add the two numbers and return the sum as a linked list
        :return:
        """
        if not self.chack_digits():
            raise Exception("Введенное число должно быть больше 0 и меньше 9.")

        # converting list to integer
        int_l1 = self.convert_to_integer(self.list1)
        int_l2 = self.convert_to_integer(self.list2)

        # adding
        if not int_l1 and not int_l2:
            raise AttributeError("Invalid attribute")

        total_int = int_l1 + int_l2
        total_list = list(reversed(str(total_int)))

        # output
        output = f"Input: l1 = {self.list1}, l2 = {self.list2}\n"
        output += f"Output: {total_list}\n"
        output += f"Explanation: {int_l1} + {int_l2} = {total_int}"

        return output

    def convert_to_integer(self, lst = None):
        """
        Converting handle list to integer, for adding each other
        :param lst:
        :return:
        """
        if lst != None and type(lst) == list:
            convert_string = [str(number) for number in list(reversed(lst))]
            string = "".join(convert_string)
            integer = int(string)
            return integer
        else:
            return False

#
# list_1 = [2,4,3]
# list_2 = [5,6,4]
#
# cls = MyList(list_1, list_2)
# r = cls.revers()
# print(r)

