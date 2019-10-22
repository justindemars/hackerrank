if __name__ == '__main__':
    s = input()

for test in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print(any(test(c) for c in s))
