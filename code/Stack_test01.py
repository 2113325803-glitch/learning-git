def check(text: str) -> bool:
    # 1. 定义映射关系：右括号对应正确的左括号
    pairs = {')': '(', ']': '[', '}': '{'}       #键值对：  用关键字来找值，用值来找关键字
    
    # 2. 初始化栈
    stack = []
    
    # 3. 遍历字符串
    for char in text:
        # 如果是左括号，入栈
        if char in '([{':
            stack.append(char)
            
        # 如果是右括号
        elif char in ')]}':
            # 情况 A：栈为空，说明没有对应的左括号，直接失败
            if not stack:    
                return False
                
            # 情况 B：弹出栈顶，检查是否匹配
            top = stack.pop()      #pop()是移除栈顶元素，返回栈顶元素
            if top != pairs[char]:  #现在的char值在pairs里面找对应的键值，如果键值等于top，说明匹配，否则不匹配
                #！=是不等于，如果键值不等于top，说明不匹配
                return False
                
        # 其他字符（如字母、数字），直接忽略
        else:
            continue
            
    # 4. 循环结束后，如果栈为空，说明全部匹配，返回 True；否则返回 False
    return len(stack) == 0


# ================= 测试用例 =================
if __name__ == "__main__":
    # print(check("(a[b]{c})"))   # True
    # print(check("(a[b)]"))      # False
    # print(check("((("))         # False
    # print(check(""))            # True
    # print(check(")"))           # False
    #print(check("{[()]}"))      # True
    # print(check("([)]"))        # False
    # print(check("hello"))       # True
    print(check("{(){}[]}"))