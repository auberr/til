def solution(left, right):
    answer = 0
    left_list = []
    for i in range(1, left+1):
        for j in range(1, left+1):
            if left % j == 0:
                if j not in left_list:
                    left_list.append(j)

    # print(left_list)
    # print(len(left_list))

    num_list_check = []
    for i in range(left, right+1):
        num_list = []
        for j in range(1, i+1):
            if i % j == 0:
                if j not in num_list:
                    num_list.append(j)
        print(num_list)
        if len(num_list) % 2 == 0:
            num_list_check.append(i)
        elif len(num_list) % 2 == 1:
            num_list_check.append(-i)
        

    print(num_list_check)

    return sum(num_list_check)

print(solution(13, 17))


cnt = 0
a = 4

for i in range(1, a+1):
    if a % i == 0:
        cnt +=1;
print(cnt)

cnt = 0
a = 4

for i in range(1, a+1):
    if a % i == 0:
        cnt +=1;
    
print("약수 개수", cnt)

if cnt % 2 == 0:
    print("약수 개수 짝")
else:
    print("약수 개수 홀")