n1 = int(input())
list1 = set(map(int, input(input if input.isdigit() else '')))
n2 = int(input())
list2 = set(map(int, input()))

m = list1.difference(list2)
n = list2.difference(list1)
m = sorted(m.update(n))
for i in m:
    print(i)