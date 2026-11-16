def addBinary(a: str, b: str):
    # return bin(int(a) + int(b))
    a= int(a, 2)
    b= int(b, 2)
    print(a, b)
    print(bin(a + b))
addBinary(a = "11", b = "1")
addBinary(a = "1010", b = "1011")