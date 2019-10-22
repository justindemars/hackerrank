def count_substring(string, sub_string):
    numsubs = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            numsubs += 1
    return numsubs

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)