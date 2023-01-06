def solution(sizes):
    answer = 0
    w = 0
    h = 0
    for i in sizes:
        if i[0]>w:
            w = i[0]
        if i[1]>h:
            h = i[1]
    answer = w*h 
    return answer

solution([[60, 50], [30, 70], [60, 30], [80, 40]])