def mutate_string(string, position, character):
    mut = list(string)
    mut[position] = character
    new_s = ''.join(mut)
    return new_s

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)