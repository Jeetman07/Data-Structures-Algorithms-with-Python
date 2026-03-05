def simplify_path(path):
    parts = path.split("/")
    stack = []
    for p in parts:
        if p == "" or p == ".":
            continue
        if p == "..":
            if stack:
                stack.pop()
        else:
            stack.append(p)
    return "/" + "/".join(stack)

path = "/home//user/.././docs"
print("Input:", path)
print("Output:", simplify_path(path))