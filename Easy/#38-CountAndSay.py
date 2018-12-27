def read_num(num):
    """
    num: string
    """
    count = 0
    string = ""
    check = num[0]

    for digit in num:
        if check == digit:
            count += 1
        else:
            string += str(count) + check
            check = digit
            count = 1
    string += str(count) + check
    return string


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        prev_ans = "1"

        for i in range(1, n):
            prev_ans = read_num(prev_ans)
        print(prev_ans)
        return prev_ans



if __name__ == '__main__':
    n = 4
    solution = Solution()
    solution.countAndSay(n)