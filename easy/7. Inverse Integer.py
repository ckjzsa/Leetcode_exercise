class Solution:
    def reverse(self, x: int) -> int:
        number = str(x)

        if len(number) == 1:
            return x

        string = ""
        if number[0] == '-':
            string += "-"
            number = number.strip("-")

        for num in number[::-1]:
            string += num

        if int(string) > (2**31 -1) or int(string) < (-2**31):
            return 0
        else:
            return int(string)
