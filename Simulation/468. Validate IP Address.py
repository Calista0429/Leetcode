
def validIPAddress(queryIP: str) -> str:

    ip = queryIP.split('.')
    if len(ip) == 4:
        for sub in ip:
            if not sub or not sub.isdigit():
                return "Neither"
            elif sub[0] == '0' and len(sub) > 1:
                return "Neither"
            elif int(sub) > 255 or int(sub) < 0:
                return "Neither"
        return "IPv4"
    ip = queryIP.split(":")
    if len(ip) == 8:
        valid = "0123456789abcdefABCDEF"
        for sub in ip:
            if not sub:
                return "Neither"
            elif len(sub) > 4:
                return "Neither"
            for s in sub:
                if s not in valid:
                    return "Neither"
        return "IPv6"
    return "Neither"
        


        
        



        


        
    