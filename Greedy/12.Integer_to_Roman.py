def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    r_map = {"I":1, "V":5, "X":10, "L": 50, "C": 100, "D": 500, "M":1000, "IV": 4, "IX": 9, "XC":90, "XL":40, "CD":400, "CM":900}
    sorted_map = dict(sorted(r_map.items(), key=lambda item:item[1], reverse=True))
    # sorted_map = sorted(r_map.items(), key=lambda item:item[1], reverse=True)
    res = ""
    print(sorted_map)
    for sym, val in sorted_map.items():
        if num // val:
            count = num // val
            res += (sym * count)
            num %= val
    return res

intToRoman(3749)