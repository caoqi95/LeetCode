def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    s = int(str(abs(x))[::-1])
    return True if s == x else False




if __name__ == '__main__':
    isPalindrome(10101)