def is_prime_number_3(n):
    arr = [True] * (n+1)
    arr[0] = False
    arr[1] = False
    
    for i in range(2, n+1):
        if arr[i] == True:
            j = 2
            
            while (i * j) <= n:
                arr[i*j] = False
                j+=1
    return arr

arr = is_prime_number_3(50)

for i in range(len(arr)):
    if arr[i] == True:
        print(i, end=' ')


import math

def is_prime_number_2(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

print(is_prime_number_2(15))

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print(is_prime_number(15))








input = 20

def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        print(n, '-------------------')
        for i in prime_list:
            print(n, i, '+++++++++++++++++++')
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)


def find_prime(number):
    prime_list = []
    for n in range(2, number+1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            prime_list.append(n)
    return prime_list

result = find_prime(input)
print(result)


def find_prime_list_under_number(number):
    # 1. 1부터 자기 자신까지 반복문을 돈다.
    answer = []
    for i in range(2, number+1):
        for j in range(2, i+1):
            if i != j and i % j == 0:
                print(i, j)
                break
            if i%j ==0 and i not in answer:
                print(i, j, '-----')
                answer.append(i)
    
    # 2. 반복문을 돌면서 나눠서 1과 자기자신만을 약수로 갖는지 확인한다.
    # 3. 그렇다고 하면 answer 리스트에 추가한다.
    return answer


result = find_prime_list_under_number(input)
print(result)