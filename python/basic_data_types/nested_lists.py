if __name__ == '__main__':
    scores= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([score, name])

    scores.sort()

    a = [i for i in scores if i[0] != scores[0][0]]
    b = [j for j in a if j[0] == a[0][0]]

    b.sort(key=lambda x: x[1])
    for i in range(len(b)):
        print(b[i][1])