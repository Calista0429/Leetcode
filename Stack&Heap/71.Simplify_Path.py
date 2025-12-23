def simplifyPath(path: str) -> str:
    stack = []
    files = path.split("/")
    for file in files:
        if file == "" or file == ".":
            continue

        if file == "..":
            if stack:
                stack.pop()
        
        else:
            stack.append(file)
    
    return "/" + "/".join(stack)



simplifyPath(path = "/home/user/Documents/../Pictures")

simplifyPath(path = "/.../a/../b/c/../d/./")
