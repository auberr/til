## 1. 조건문

### 요구조건

# - 사용자의 시험 점수를 입력받아 등급을 출력하는 코드를 만들어주세요
#     - 등급표
#         - 91~100 : A
#         - 81~90 : B
#         - 71~80 : C
#         - ~71 : F

# 입출력 예제
# def get_grade(score):
#     # some code

# score = int(input())
# grade = get_grade(score)
# print(grade) # A ~ F


# print("1~100점 까지의 점수를 입력해주세요")
# print("등급표에 맞는 점수를 출력합니다.")

# def get_grade(score):
#     if 91 < score <=100:
#         grade = "A"
#         return grade
#     elif 81 < score <=90:
#         grade = "B"
#         return grade
#     elif 71 < score <=80:
#         grade = "C"
#         return grade
#     elif score < 70:
#         grade = "F"
#         return grade

# try:
#     score = int(input())
#     print(f"귀하의 등급은 {get_grade(score)} 입니다.")
# except ValueError:
#     print("잘못된 값을 입력하셨습니다.")
# except NameError:
#     print("잘못된 값을 입력하셨습니다.")


## 2. 반복문(while)

### 요구조건

# - 사용자의 입력을 받아 반복하는 프로그램을 만들어주세요
# - 사용자가 숫자를 입력했을 경우 입력값에 2배를 곱한 수를 출력해주세요
# - 사용자가 문자를 입력했을 경우 “입력한 문자는 {} 입니다.” 라는 문구를 출력해주세요
#     - {} 자리에는 사용자가 입력한 문자가 들어가야 합니다.
# - 사용자가 exit을 입력하거나 숫자가 5회 이상 입력됐을 경우 프로그램을 종료시켜주세요


# user_int = 0

# while True:
#     user = input()
    
#     if user.isdecimal() == True:
#         output = int(user) * 2
#         print(output)
#         user_int+=1
        
#         if user_int >= 5:
#             break
#         elif user =="exit":
#             break

#     elif type(user) == type("a"):
#         print(f"입력한 문자는{user}입니다.")

#         if user_int >= 5:
#             break
#         elif user =="exit":
#             break
    

## 3. 반복문(for)

### 요구조건

# - 입출력 예제에 있는 사람들 중, 평균 성적이 70점 이상인 사용자의 이름과 나이를 출력해주세요

from pprint import pprint

users = [
    {"name": "Ronald", "age": 30, "math_score": 93, "science_score": 65, "english_score": 93, "social_score": 92},
    {"name": "Amelia", "age": 24, "math_score": 88, "science_score": 52, "english_score": 78, "social_score": 91},
    {"name": "Nathaniel", "age": 28, "math_score": 48, "science_score": 40, "english_score": 49, "social_score": 91},
    {"name": "Sally", "age": 29, "math_score": 100, "science_score": 69, "english_score": 67, "social_score": 82},
    {"name": "Alexander", "age": 30, "math_score": 69, "science_score": 52, "english_score": 98, "social_score": 44},
    {"name": "Madge", "age": 22, "math_score": 52, "science_score": 63, "english_score": 54, "social_score": 47},
    {"name": "Trevor", "age": 23, "math_score": 89, "science_score": 88, "english_score": 69, "social_score": 93},
    {"name": "Andre", "age": 23, "math_score": 50, "science_score": 56, "english_score": 99, "social_score": 54},
    {"name": "Rodney", "age": 16, "math_score": 66, "science_score": 55, "english_score": 58, "social_score": 43},
    {"name": "Raymond", "age": 26, "math_score": 49, "science_score": 55, "english_score": 95, "social_score": 82},
    {"name": "Scott", "age": 15, "math_score": 85, "science_score": 92, "english_score": 56, "social_score": 85},
    {"name": "Jeanette", "age": 28, "math_score": 48, "science_score": 65, "english_score": 77, "social_score": 94},
    {"name": "Sallie", "age": 25, "math_score": 42, "science_score": 72, "english_score": 95, "social_score": 44},
    {"name": "Richard", "age": 21, "math_score": 71, "science_score": 95, "english_score": 61, "social_score": 59},
    {"name": "Callie", "age": 15, "math_score": 98, "science_score": 50, "english_score": 100, "social_score": 74},
]

# def set_score(**kwargs):
#     profile = {}
#     profile["name"] = kwargs.get("name", "-")
#     profile["name"] = kwargs.get("name", "-")
#     profile["name"] = kwargs.get("name", "-")
#     profile["name"] = kwargs.get("name", "-")
#     profile["name"] = kwargs.get("name", "-")





user_avg = 0
filter_users=[]

# users_list.append(users[i]['age'])

for i in range(len(users)): #인덱스 대신 바로 user 를 바로 씀
    user_avg = (users[i]['math_score'] + users[i]['science_score'] + users[i]['english_score'] + users[i]['social_score'])/4
    
    if user_avg > 70:
        filter_users.append({"age": users[i]['age'], "name": users[i]['name']})
        #여기에 딕셔너리를 하나 만들어본다 중괄호 열고 데이터) #딕셔너리를 하나 새로 만들어서 넣는다
        #append 안에 중괄호 
    
pprint(filter_users)



    

# def get_filter_user(users):
#     for i in **users:

#     return filter_user

