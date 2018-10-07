def longestCommonPrefix(strs):
    """
    :param strs:
    :return: string
    """
    # 如果字符串列表为空，则返回 ""
    if not strs :return ""

    # 找出字符串中最大和最小的元素
    s1 = min(strs)
    s2 = max(strs)

    for i, c in enumerate(s1):
        # 如果 s1 中的字符与 s2 对应位置的字符不一样，返回前面一样的字符
        if c!= s2[i]:
            print(s1[:i])
            return s1[:i]

    return s1



if __name__ == '__main__':
    strs = {"flower", "fow", "flight"}
    longestCommonPrefix(strs)