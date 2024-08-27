def reverse_string(s: str) -> str:
    # 基本情况：如果字符串为空或只有一个字符
    if len(s) <= 1:
        return s
    # 递归情况：返回最后一个字符 + 反转剩余字符串
    return s[-1] + reverse_string(s[:-1])

# 测试
input_string = "hello"
reversed_string = reverse_string(input_string)
print(f"Original String: {input_string}")
print(f"Reversed String: {reversed_string}")