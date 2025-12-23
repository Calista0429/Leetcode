def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    res = 0
    for i in range(len(tokens)):
        if tokens[i] not in "+-*/":
            stack.append(int(tokens[i]))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if tokens[i] == '+':
                res = num1 + num2
            elif tokens[i] == '-':
                res = num2 - num1
            elif tokens[i] == '*':
                res = num1 * num2
            else:
                if num2 != 0:
                    res = int(num2 / num1)
            stack.append(res)
    return stack[0]
                
# evalRPN(tokens = ["2","1","+","3","*"])
# evalRPN(tokens = ["4","13","5","/","+"])
evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    

    