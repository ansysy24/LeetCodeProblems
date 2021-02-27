def shortenPath(path):
    absolute = False
    if path.startswith('/'):
        absolute = True

    path = path.split('/')
    stack = []
    for char in path:
        if char in ['', '.']:
            pass
        elif char == '..':
            if absolute:
                if stack:
                    stack.pop()
            else:
                if stack and stack[-1] != '..':
                    stack.pop()
                else:
                    stack.append(char)
        else:
            stack.append(char)

    result = '/'.join(stack)
    if absolute:
        result = '/' + result
    return result

print(shortenPath("/foo/../test/../test/../foo//bar/./baz"))