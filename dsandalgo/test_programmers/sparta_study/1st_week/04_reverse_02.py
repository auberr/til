def solution(n):
    answer = []
    answer_list = list(str(n))
    answer_list.reverse()
    answer = [int(i) for i in answer_list]
    return answer
    

print(solution(12345))

def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)));