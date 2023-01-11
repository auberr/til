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