import textwrap

def wrap(string, max_width):
    length = len(string)
    temp = [string[i:  i + max_width] for i in range(0,len(string), max_width) ]
    string = '\n'.join(temp)
    return string
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)