input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0
    
    if string[0] == '0':
        count_to_all_one +=1
    elif string[0] == '1':
        count_to_all_zero +=1
    
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == '0':
                count_to_all_one+=1
            elif string[i+1] == '1':
                count_to_all_zero+=1
    return min(count_to_all_zero, count_to_all_one)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

# s = input()

# change_0 = 0
# change_1 = 0

# if s[0] == '0' :
#   change_1 += 1
# else :
#   change_0 += 1

# for i in range(len(s) - 1) :
#   if s[i] != s[i+1] :
#     if s[i+1] == '0' :
#       change_1 += 1
#     else :
#       change_0 += 1

# print(min(change_0, change_1))


# 0 -> 0번 바뀜 -> 0번 뒤집음
# 01 -> 1번 바뀜 -> 1번 뒤집음
# 010 -> 2번 바뀜 -> 1번 뒤집음
# 0101 -> 3번 바뀜 -> 2번 뒤집음
# 01010 -> 4번 바뀜 -> 2번 뒤집음
# 010101 -> 5번 바뀜 -> 3번 뒤집음
# 0101010 -> 6번 바뀜 -> 3번 뒤집음


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    count = 0

    for i in range(0, len(string)-1):
        if string[i] != string[i+1]:
            count+=1
    
    return (count+1)//2


print(find_count_to_turn_out_to_all_zero_or_all_one("0001100"))
print(find_count_to_turn_out_to_all_zero_or_all_one("11111"))
print(find_count_to_turn_out_to_all_zero_or_all_one("00000001"))
print(find_count_to_turn_out_to_all_zero_or_all_one("11001100110011000001"))
print(find_count_to_turn_out_to_all_zero_or_all_one("11101101"))
