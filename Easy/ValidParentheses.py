def isVaild(s):
    """
    :param s: string
    :return: bool
    """
    # 建立一个空的堆栈
    stack = []

    # 建立一个哈希映射，这将使得代码非常简单，如果要添加其他类型的括号，添加也很容易
    mapping = {")":"(", "]":"[", "}":"{"}

    # 对于 s 中所有的字符
    for char in s :

        # 如果为右括号
        if char in mapping:

            # 如果堆栈非空，则弹出堆栈中的顶部元素，否则 top_element 设定为“#”
            top_element = stack.pop() if stack else "#"

            # 如果哈希映射中的左括号与顶部元素不相等，则返回 False
            if mapping[char] != top_element:
                return False

        # 如果为左括号则直接添加至堆栈中
        else:
            stack.append(char)

    # 最后堆栈为空，则是一个有效的字符串
    return not stack


if __name__ == "__main__":
    s = "([]){}"
    isVaild(s)