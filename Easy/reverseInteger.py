# solution 1, my own solution
# run time: 116ms
def reverse(x):
    """
    :param x: int
    :return: int
    """
    x_abs = abs(x)
    a = []
    for i in range(0, len(str(x_abs))):
        m = int(x_abs /(10**i))
        ones_place = m % 10
        a.append(ones_place)
    # print(a)
    r = 0
    for i in range(0, len(a)):
        r += a[i]*10**(len(a)-(i+1))
    if x < 0 and -r >= -2**31:
        # print(-r)
        return -r
    elif x > 0 and r <= 2**31 -1 :
        # print(r)
        return r
    else:
        # print(0)
        return 0

# solution 2, from other's solution，it's pythonic.
# run time: 60ms
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        s = int(str(abs(x))[::-1])
        # print(s)
        if s > 2147483647 or s < -2147483648:
            return 0
        return s if x > 0 else -s
