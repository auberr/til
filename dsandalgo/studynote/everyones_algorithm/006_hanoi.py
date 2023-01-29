count=0
def hanoi(n, from_pos, to_pos, aux_pos):
    # 원반이 1개 일때는 그냥 옮김
    if n == 1:
        print(from_pos, "->", to_pos)
        return
    # 원반 n-1개를 aux_pos 로 이동 (to_pos를 보조 기둥으로)
    count+=1
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    print(from_pos, "->", to_pos)
    count+=1
    hanoi(n - 1, aux_pos, to_pos, from_pos)
    return count

# print("n = 1")
# print(hanoi(1, 1, 3, 2))
# print("n = 2")
# print(hanoi(2, 1, 3, 2))
# print("n = 3")
# print(hanoi(3, 1, 3, 2))
# print("n = 4")
# print(hanoi(4, 1, 3, 2))
print("n = 5")
print(hanoi(5, 1, 3, 2))
