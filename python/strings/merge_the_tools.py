def merge_the_tools(string, k):
    l = [string[i:i+k] for i in range(0, len(string), k)]
    # result = [n for m in l for n in m if m not in l]
    result = ''
    for j in l:
        result += find_unique(j) + '\n'
    print(result)

def find_unique(s):
    result = ''
    for i in s:
        if i not in result:
            result+=i
    return result


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)