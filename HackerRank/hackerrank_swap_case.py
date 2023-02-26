def swap_case(s):
    sn = ''
    for char in s:
        if char.islower():
            sn += char.upper()
        elif char.isupper():
            sn += char.lower()
        else:
            sn += char
        
    return sn

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)