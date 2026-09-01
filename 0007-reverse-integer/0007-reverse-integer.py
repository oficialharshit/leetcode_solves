class Solution(object):
    def reverse(self,x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while x > 0:
            digit = x % 10

            # Check overflow before multiplying by 10
            if reversed_num > INT_MAX // 10:
                return 0

            if reversed_num == INT_MAX // 10 and digit > INT_MAX % 10:
                return 0

            reversed_num = reversed_num * 10 + digit
            x //= 10

        reversed_num *= sign

        # Final range check
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num