## solution
## from other's solution

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    values = {
            "I" : 1, "V": 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000
        }
    high = 0                        # highest value we have seen
    result = 0                      # final result
    for letter in s[::-1]:          # letter in reverse order
        value = values[letter]      # integer value of the letter
        if value >= high:           # we found a value >= high and we sum it
            high = value            # record the new high
            result += value         # add value to result
        else:                       # we found a value < high so we subtract
            result -= value         # remove value from result
    print(result)

    return result


if __name__ == '__main__':
    romanToInt("MCMXCIV")