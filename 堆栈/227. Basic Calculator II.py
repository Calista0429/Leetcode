def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    st = []
    i = 0
    op = "+"
    s = s.strip()
    while i < len(s):
        if s[i].isdigit():
            num = s[i]
            while i + 1 < len(s) and s[i + 1].isdigit():
                num += s[i+1]
                i += 1
            num = int(num)
            if op == "+":
                st.append(num)
            elif op == "-":
                st.append(-num)
            elif op == "*":
                top = st.pop()
                st.append(top * num)
            elif op == "/":
                top = st.pop()
                st.append(int(top / num))
        else:
            if s[i] in "+-*/":
                op = s[i]
        i += 1
    return sum(st)

# calculate("3+2*2")  # 7
# calculate(" 3/2 ")  # 1
# calculate(" 3+5 / 2 ")  # 5
calculate("-3/2")   # 13
