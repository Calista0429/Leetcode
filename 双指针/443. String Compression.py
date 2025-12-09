def compress(chars):

    res = ""
    left = 0
    if len(chars) == 1:
        return 1
    while left < len(chars):
        right = left + 1
        while right < len(chars) and chars[left] == chars[right]:
            right += 1
        if right == len(chars):
            res += chars[left]
            length = right - left
            if length != 1:
                res += str(length)
            break
        if chars[right] != chars[left]:
            res += chars[left]
            length = right - left
            if length != 1:
                res += str(length)
            left = right
    chars[:] = list(res)
    return len(chars)

# chars = ["a","a","b","b","c","c","c"]
# chars  = ["a"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","b","c"]
print(compress(chars))