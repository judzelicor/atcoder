class Solution:
    def solve(self, number: int):
        """
        The ones digit of an integer N is the remainder when N is divided by 10.
        The tens digit of an integer N is the quotient when N is divided by 100
        and the remainder of this operation is divided by 10.
        """
        ones = number % 10
        tens = (number % 100) // 10
        return f"{tens}{ones}"



solution = Solution()


# Test


# If the number is 254, it should return the string 54 as they are the last two digits of the number.
assert solution.solve(254) == "54"


# If the number is 304, it should return the string 04, not 4, as they are the last two digits of the number.
assert solution.solve(304) == "04"


# If the number is 21, it should return the string 21, as they are the last two digits of this two digit number.
assert solution.solve(21) == "21"



