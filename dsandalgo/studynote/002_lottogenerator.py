import random

# 1번 예시 코드
# lotto = set()
# bonus = set()

# def lotto_number_generator(count):
#     result = []
#     if count < 1:
#         print("1 이상의 값을 입력해주세요")
#         return False

#     for i in range(count):
#         lotto_numbers = set()
#         bonus_numbers = set()
        
#         while len(lotto_numbers) < 6:
#             lotto_numbers.add(random.randint(1, 45))
        
#         bonus_numbers.add(random.randint(1, 45))
        
#         result.append(lotto_numbers)
#         result.append(bonus_numbers)
        
#     return result

# lotto_numbers = lotto_number_generator(1)
# print(lotto_numbers)


# 2번 예시 코드
from pprint import pprint

def lotto_number_generator(count):
    result = []
    if count < 1:
        print("1 이상의 값을 입력해 주세요")
    
    for i in range(count):
        lotto_numbers = set()
        
        while len(lotto_numbers)< 8:
            lotto_numbers.add(random.randint(1, 45))
            
        result.append(lotto_numbers)
    
    return result

lotto_numbers = lotto_number_generator(int(input("몇개나 뽑을까요?")))
pprint(lotto_numbers)


# # 내 코드
# def lotto_number(input):
#     # 1. 45까지의 배열을 만든다.
    
#     numbers = [x for x in range(1, 46)]
#     # print(numbers)
    
#     # 2. 45까지의 배열 중 랜덤으로 6개를 뽑는다.
    
#     lotto_number_list = set()
#     while True:
#         lotto_number_list.add(random.randrange(1, 45))
#         if len(lotto_number_list) == 6:
#             break
    
#     new_list = []
#     for i in lotto_number_list:
#         new_list.append(i)
    
#     (new_list).sort()
    
#     # 3. 나머지 숫자 중 보너스 숫자를 하나 뽑는다.
    
#     bonus_nummber_list = []
    
#     while True:
#         bonus_number = random.randint(1, 45)
#         if bonus_number not in lotto_number_list:
#             bonus_nummber_list.append(bonus_number)
#             break    
    
#     # 4. 리턴
#     return new_list, bonus_nummber_list
    
# print(lotto_number(input))