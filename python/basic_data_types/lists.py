if __name__ == '__main__':
    N = int(input())
    new_arr = []
    for _ in range(N):
        cmd = input()
        cmd = cmd.split()
        if "insert" in cmd:
            new_arr.insert(int(cmd[1]), int(cmd[2]))
        elif "print" in cmd:
            print(new_arr)
        elif "remove" in cmd:
            new_arr.remove(int(cmd[1]))
        elif "append" in cmd:
            new_arr.append(int(cmd[1]))
        elif "sort" in cmd:
            new_arr.sort()
        elif "pop" in cmd:
            new_arr.pop()
        elif "reverse" in cmd:
            new_arr.reverse()