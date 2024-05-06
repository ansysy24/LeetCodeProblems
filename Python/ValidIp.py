def validIPAddresses(string):
    addresses = []
    for i in range(1, min(len(string), 4)):
        current_address = ['', '', '', '']
        current_address[0] = string[:i]
        if not is_valid(current_address[0]):
            continue
        for j in range(i+1, i + min(len(string)-i, 4)):
            current_address[1] = string[i:j]
            if not is_valid(current_address[1]):
                continue
            for k in range(j+1, j+  min(len(string) -j, 4)):
                current_address[2] = string[j:k]
                current_address[3] = string[k:]
                if is_valid(current_address[2]) and is_valid(current_address[3]):
                    addresses.append('.'.join(current_address))
    return addresses

def is_valid(num):
    if len(num) != len(str(int(num))):
        return False
    return int(num) < 256

print(validIPAddresses('123456'))