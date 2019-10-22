def wrap(string, max_width):
    s = ''
    for i in range((len(string) // max_width) + 1):
        s = s + string[i*max_width:(i+1)*max_width] + '\n'
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)