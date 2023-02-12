def solution(arr):
    answer = []

    # 가장 작은 수를 제거한 배열 리턴
    # 가장 작은 수를 구한다.
    minimum = arr[0]

    # 가장 작은 수와 전체 배열을 돌면서 비교
    i=0
    while i < len(arr):
        if arr[i] < minimum:
            minimum = arr[i]
        i+=1
        print(minimum)

    # 가장 작은 수를 배열에서 제거 한다.
    for i in arr:
        if i == minimum:
            arr.remove(i)

    answer = arr

    # 빈 경우 -1 을 리턴
    if answer == []:
        return [-1]
    else:
        return answer


# a = solution([4, 3, 2, 1])
a = solution([10])


print(a)