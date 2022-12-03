def solution(numbers):
    answer=0
    for i in numbers:
        if i not in numbers:
            answer+=i
    return answer


def solution(numbers):
    answer = 0
    nines = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in numbers:
        nines.remove(i)
    for i in nines:
        answer +=i
    return answer

solution([1,2,3,4,6,7,8,0])
solution([5,8,4,0,6,7,9])
	