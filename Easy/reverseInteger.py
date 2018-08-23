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
    #print(a)
    r = 0
    for i in range(0, len(a)):
        r += a[i]*10**(len(a)-(i+1))
    if x < 0 and -r >= -2**31:
        #print(-r)
        return -r
    elif x > 0 and r <= 2**31 -1 :
        #print(r)
        return r
    else:
        #print(0)
        return 0

if __name__ == '__main__':
    reverse(-32100)
