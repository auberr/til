# 문제 설명
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

# 제한 조건
# arr은 길이 1 이상인 배열입니다.
# 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.

# [4,3,2,1] -> # [4,3,2]

def solution(arr):
    answer = arr
    minimum = arr[0]
        
    for i in arr:
        if minimum > i:
            minimum = i
    arr.remove(minimum)
    
    if len(arr) == 0:
        answer = [-1]
    
    return answer

print(solution([4,3,2,1]))

print(solution([1]))


def bubbleSort(arr):
    for front_index in range(0, len(arr) - 1): # 0, 1, 2
        for index in range(front_index+1, len(arr)): # 1, 2, 3
            if arr[front_index] > arr[index]:
                temp = arr[front_index]
                arr[front_index] = arr[index]
                arr[index] = temp
            # print(f"{index}번 바꿔봅시다 {arr}") # 9번 실행
    return arr