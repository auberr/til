def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # 1. 앞과 뒤의 숫자를 비교해서 같은 수가 나오면 pass 하고 다른 수가 나오면 앞의 숫자를 넣는다. 
    for i in range(len(arr)):
        if i-1>=0:
            print(i, len(arr), "---")
            print(arr[i-1], arr[i])
            if arr[i-1] != arr[i]:
                answer.append(arr[i-1])
            if int(i) == int(len(arr)-1):
                answer.append(arr[i])
            if arr[i-1] == arr[i]:
                pass
            

    # 2. 마지막 비교 대상은 넣는다. 
    
    return answer

print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))