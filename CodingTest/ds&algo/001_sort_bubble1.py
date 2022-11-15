# 버블 (거품) 정렬

'''
핵심로직:
1. 자리바꾸기 : 첫번째거(n)랑 두번째거(n+1)랑 비교해서 두번째거가 더 작으면 첫번째거랑 자리를 바꾼다.
https://www.youtube.com/watch?v=53FCnMP1-4o&list=PLAdQRRy4vtQRwAGymS3q3VXk1WUfhZg7l&index=4
'''

1.
#처음 리스트
numbers = [7, 3, 2, 9]

#비교하기
first = numbers[0] # 7
second = numbers[1]
print(first, second)
print(first > second)

# 비교해서 큰수가 뒤로 가게 자리 바꾸기
temp = first
first = second
second = temp
print(first, second)

'''
핵심로직:
2. 규칙찾기
https://www.youtube.com/watch?v=jMniubX8ojA
'''
#처음 리스트
numbers = [7, 3, 2, 9]

# 한번 바꿈 ->
numbers = [3, 7, 2, 9]

#비교하기
first = numbers[0]
third = numbers[2]
print(first, third)

# 비교해서 큰수가 뒤로 가게 자리 바꾸기
temp = first
first = third
third = temp
print(first, third)

# 한번 바꿈 ->
numbers = [2, 7, 3, 9]

first = numbers[0]
fourth = numbers[3]
print(first, fourth)

#비교해서 바꿀것이 없음

#처음 리스트
# n = 1
numbers = [7, 3, 2, 9]  # 
numbers = [3, 7, 2, 9]  # n(1) n(1)+1 = 1, 2
numbers = [2, 7, 3, 9]  # n(1) n(1)+2 = 1, 3
numbers = [2, 7, 3, 9]  # n(1) n(1)+3 = 1, 4

'''
핵심로직:
3. 규칙을 통해서 반복문으로
https://www.youtube.com/watch?v=Srsa2WXWwRA
'''

numbers = [7, 3, 2, 9]

if numbers[0] > numbers[1]: # 7 > 3
    # 자리를 바꾼다.
    temp = numbers[0]
    numbers[0] = numbers[1]
    numbers[1] = temp

print(numbers)
# [7, 3, 2, 9] => [3, 7, 2, 9]


if numbers[0] > numbers[2]: # 3 > 2
    # 자리를 바꾼다.
    temp = numbers[0]
    numbers[0] = numbers[2]
    numbers[2] = temp

print(numbers)
# [3, 7, 2, 9] => [2, 7, 3, 9]

numbers = [7, 3, 2, 9]

for index in range(1, len(numbers)):
    if numbers[0] > numbers[index]:
        temp = numbers[0]
        numbers[0] = numbers[index]
        numbers[index] = temp
    print(f"{index}번 바꾸면 {numbers}")

# numbers = [7, 3, 2, 9]
# 1번 바꾸면 [3, 7, 2, 9]
# 2번 바꾸면 [2, 7, 3, 9]
# 3번 바꾸면 [2, 7, 3, 9]

# 0 번째와 나머지를 모두 비교를 한다.
# 1바퀴를 돌면 가장 작은게 0번째에 온다.

numbers = [2, 7, 3, 9]
        # [2, 3, 7, 9]  1번 바꾸면
        # [2, 3, 7, 9]  2번 바꾸면
        # [2, 3, 7, 9]  3번 바꾸면

for index in range(2, len(numbers)):
    if numbers[1] > numbers[index]:
        temp = numbers[1]
        numbers[1] = numbers[index]
        numbers[index] = temp
    print(f"{index}번 바꾸면 {numbers}")


numbers = [2, 3, 7, 9]
        # [2, 3, 7, 9]  1번 바꾸면

for index in range(3, len(numbers)):
    if numbers[2] > numbers[index]:
        temp = numbers[2]
        numbers[2] = numbers[index]
        numbers[index] = temp
    print(f"{index}번 바꾸면 {numbers}")


# -> 그다음 풀어야할 문제
# 그다음 작은게 1번째 와야 한다.



'''
핵심로직:
4. 규칙을 통해서 반복문으로
https://www.youtube.com/watch?v=Srsa2WXWwRA
'''


numbers = [7, 3, 2, 9]
# front_index 가 0일때 1,2,3
# front_index 가 1일때 2, 3
# front_index 가 2일때 3

for front_index in range(0, len(numbers) - 1): # 0, 1, 2
    for index in range(front_index+1, len(numbers)): # 1, 2, 3
        if numbers[front_index] > numbers[index]:
            temp = numbers[front_index]
            numbers[front_index] = numbers[index]
            numbers[index] = temp
        print(f"{index}번 바꿔봅시다 {numbers}") # 9번 실행


'''
함수로
'''




def bubbleSort(arr):
    for front_index in range(0, len(arr) - 1): # 0, 1, 2
        for index in range(front_index+1, len(arr)): # 1, 2, 3
            if arr[front_index] > arr[index]:
                temp = arr[front_index]
                arr[front_index] = arr[index]
                arr[index] = temp
            # print(f"{index}번 바꿔봅시다 {arr}") # 9번 실행
    return arr

result = bubbleSort(arr = [7, 3, 2, 9])
print(result)