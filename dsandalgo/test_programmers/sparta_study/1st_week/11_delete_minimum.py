def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    else:
        minimum = arr[0]
        for i in arr:
            if i < minimum:
                minimum = i
        arr.remove(minimum)
        answer = arr
    return answer

solution([4, 3, 2, 1])