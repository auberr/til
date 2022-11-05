# 1. 평균 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12944

arr =[1,2,3,4]

def solution(arr):
    answer = 0
    sum = 0
    for i in arr:
        sum+=i
    arr_length = len(arr)
    answer = sum/arr_length
    return answer

solution(arr)