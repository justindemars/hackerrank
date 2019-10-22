if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = [x for x in arr]
    l.sort()
    remove_max = [i for i in l if i != l[-1]]
    runner_up = remove_max[-1]
    print(runner_up)