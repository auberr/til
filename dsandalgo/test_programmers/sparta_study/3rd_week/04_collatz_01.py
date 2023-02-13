def solution(num):
    answer = 0
    # 주어진 수가 1인 경우에는 0을 반환
    if num == 1:
        return 0

    # 1일 될때까지 반복
    work = 0 
    while work <= 500:
        # 입력된 수가 짝수라면 2로 나눔
        if num % 2 == 0:
            num = num / 2

        # 입력된 수가 홀수라면 3을 곱하고 1을 더함
        elif num % 2 == 1:
            num = num * 3 + 1
        
        work+=1

        if num == 1:
            answer = work
            return answer

    # 작업이 500번이 될때까지 1이 안된다면 -1을 반환
    return -1