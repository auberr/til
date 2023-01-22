# 2750

N = int(input())

list=[int(input()) for i in range(N)]

sorted(list)

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

for i in list:
    print(i)


# 2751

