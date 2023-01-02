list = [9, 22, 3, 7, 4, 5]
# print(max(list))
# print(min(list))

def solution_max(list):
    result = list[0]
    for num in list[1:]:
        if result < num:
            result = num
        print(num, result)
    
    return result

def solution_max_2(list):
    result = list[0]
    for i in range(len(list)):
        if result < list[i]:
            result = list[i]
    return result


print('=>', solution_max(list))
print('=>', solution_max_2(list))