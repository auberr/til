def solution(n):
    answer = 0

    list_n = list(str(n))
    for i in list_n:
        answer+=int(i)
    print(answer)

    return answer

solution(123)

# 축약식 연습
def solution(n):
    answer = 0
    
    list_n = [int(i) for i in str(n)]
    print(sum(list_n))
    return sum(list_n)
    
solution(123)