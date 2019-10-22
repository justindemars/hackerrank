s = 'chris  alan'

def solve(s):
    s = s.split(' ')
    new_s = ''
    for i in s:
        new_s += i.capitalize() + ' '
    new_s = new_s[:-1]
    return new_s