# ## 1. 도형 넓이 계산기

# ### 요구조건

# - 인스턴스를 선언할 때 가로, 세로 길이를 받을 수 있는 클래스를 선언해 주세요
# - 인스턴스에서 사각형, 삼각형, 원의 넓이를 구하는 메소드를 생성해주세요
#     - 원의 넓이를 계산할 때는 세로 길이는 무시하고, 가로 길이를 원의 지름이라 가정하고 계산해 주세요

# 입출력 예제
# area = Area(10, 20)
# print(area.square()) # 사각형의 넓이
# print(area.triangle()) # 삼각형의 넓이
# print(area.circle()) # 원의 넓이

# import math

# math.pi

# class Area():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def square(self):
#         self.square_area = self.width * self.height
#         return self.square_area

#     def triangle(self):
#         self.triangle_area = self.width * self.height / 2
#         return self.triangle_area

#     def circle(self):
#         self.circle_area = self.width/2 * self.width/2 * math.pi
#         return self.circle_area

# area = Area(10, 20)
# print(area.square())
# print(round(area.triangle())
# print(area.circle())

# 참고 블로그 :
# [보고의 진땀나는 하루:티스토리] [Python] - 원주율 pi(π), 모듈에서 가져다 쓰기
# https://generalbulldog.tistory.com/21


## 2.  계산기 만들어보기(with class)

### 요구조건

# - 설정한 숫자를 계산해줄 클래스를 선언해주세요
# - 메소드를 호출해서 num1, num2를 설정할 수 있도록 해주세요
# - 입력된 숫자의 더하기, 빼기, 곱하기, 나누기 연산 결과를 구하는 메소드를 생성해주세요

# 입출력 예제
# calc = Calc()
# clac.set_number(20, 10)
# print(calc.plus()) # 더한 값
# print(calc.minus()) # 뺀 값
# print(calc.multiple()) # 곱한 값
# print(calc.divide()) # 나눈 값

# class Calc():
#     def __init__(self):
#         print("계산 시작")

#     def set_number(self, num1, num2):
#         self.num1 = int(num1)
#         self.num2 = int(num2)

#     def plus(self):
#         plus = self.num1 + self.num2
#         return plus

#     def minus(self):
#         minus = self.num1 - self.num2
#         return minus

#     def multiple(self):
#         multiple = self.num1 * self.num2
#         return multiple

#     def divide(self):
#         divide = self.num1 / self.num2
#         return divide
    
# a, b = map(int, input("연산할 두 수를 띄어쓰기로 입력하세요").split())
    
# calc = Calc()
# calc.set_number(a, b)
# print(f"더한값은 {calc.plus()} 입니다.")
# print(f"뺀 값은 {calc.minus()} 입니다.")
# print(f"곱한 값은 {calc.multiple()} 입니다.")
# print(f"나눈 값은 {calc.divide()} 입니다.")

#참조:
# 코딩도장 - 34.2 속성 사용하기
# https://dojang.io/mod/page/view.php?id=2373


## 3. 프로필 관리 기능 만들어보기

### 요구조건

# - 사용자들의 프로필을 관리할 수 있는 클래스를 선언해주세요
# - 메소드를 호출해서 사용자의 프로필을 설정할 수 있도록 해주세요
# - 사용자의 정보를 각각 출력할 수 있는 메소드를 만들어주세요

# 입출력 예제
# profile = Profile()
# profile.set_profile({
#     "name": "lee",
#     "gender": "man",
#     "birthday": "01/01",
#     "age": 32,
#     "phone": "01012341234",
#     "email": "python@sparta.com",
# })

# print(profile.get_name()) # 이름 출력
# print(profile.get_gender()) # 성별 출력
# print(profile.get_birthday()) # 생일 출력
# print(profile.get_age()) # 나이 출력
# print(profile.get_phone()) # 핸드폰번호 출력
# print(profile.email()) # 이메일 출력

class Profile:
    def __init__(self):
        self.profile = {
            "name": "-",
            "gender": "-",
            "birthday": "-",
            "age": "-",
            "phone": "-",
            "email": "-"
        }

    def set_profile(self, profile):
        self.profile = profile
    
    def get_profile(self):
        return self.profile

    def get_gender(self):
        return self.profile.get("gender")

    def get_birthday(self):
        return self.profile.get("birthday")
    
    def get_age(self):
        return self.profile.get("age")
    
    def get_phone(self):
        return self.profile.get("phone")
    
    def get_email(self):
        return self.profile.get("email")
    

profile1 = Profile()
profile1.set_profile({
    "name": "Chulsu Kim",
    "gender": "Male",
    "birthday": "981025",
    "age": "25",
    "phone": "821012341234",
    "email": "chulsu@gmail.com"
})

print(profile1.get_email())
print(profile1.get_gender())
print(profile1.get_birthday())
print(profile1.get_age())
print(profile1.get_phone())
print(profile1.get_email())