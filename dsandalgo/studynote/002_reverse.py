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


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    count = 0
    
    if string[0] == "0":
        for i in range(0, len(string)-1):
            print(i)
            # if string[i] != string[i+1]:
            #     count+=1
        
    elif string[0] =="1":
        for i in range(0, len(string)-1):
            if string[i] != string[i+1]:
                count+=1
    
    return count


print(find_count_to_turn_out_to_all_zero_or_all_one("0001100"))
print(find_count_to_turn_out_to_all_zero_or_all_one("11111"))
print(find_count_to_turn_out_to_all_zero_or_all_one("00000001"))
print(find_count_to_turn_out_to_all_zero_or_all_one("11001100110011000001"))
print(find_count_to_turn_out_to_all_zero_or_all_one("11101101"))
