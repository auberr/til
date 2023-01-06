def solution(array):
    return sorted(array)[len(array)//2]


def solution(array):
    answer = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            print(array[i], array[j])
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    a = len(array)//2
    answer = array[a]
    return answer

solution([1, 7, 2, 11, 10])