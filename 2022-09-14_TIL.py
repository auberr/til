# ## 1. 계산기 심화

# ### 요구조건

# - 클래스를 활용해 작성했던 계산기 코드를 활용해주세요
# - 기존처럼 사용자의 입력을 받고 출력하되, try / except를 활용해 사용자의 입력을 검증하는 코드를 추가해주세요
#     - 두 번쨰 숫자에 0을 입력하고 나누기를 시도할 경우 “0으로 나눌 수 없습니다” 문구를 출력해주세요
#     - 숫자가 아닌 다른 값을 입력했을 경우 “숫자만 입력 가능합니다” 라는 문구를 출력해 주세요

# 입출력 예제
# calc = Calc()
# clac.set_number(20, 10)
# print(calc.plus()) # 더한 값
# print(calc.minus()) # 뺀 값
# print(calc.multiple()) # 곱한 값
# print(calc.divide()) # 나눈 값


# class Calc():
#     def __init__(self):
#         pass

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

        
# try:
#     a, b = map(int, input("연산할 두 수를 띄어쓰기로 입력하세요").split())
#     calc = Calc()
#     calc.set_number(a, b)
#     calc.divide()
# except ZeroDivisionError:
#     print("0으로는 나눌 수 없습니다.")
# except NameError:
#     print("숫자만 입력 가능합니다.")
# else:
#     calc = Calc()
#     calc.set_number(a, b)
#     print(f"더한값은 {calc.plus()} 입니다.")
#     print(f"뺀 값은 {calc.minus()} 입니다.")
#     print(f"곱한 값은 {calc.multiple()} 입니다.")
#     print(f"나눈 값은 {calc.divide()} 입니다.")

# ## 2. 리스트 필터 및 정렬

# ### 요구조건

# - filter 혹은 리스트 축약식을 사용해 코드를 작성해주세요
# - 제공 된 사용자들 중 나이가 20살 미만인 사람들은 제외해주세요
# - 사용자들을 나이 순으로 정렬해주세요

# 입출력 예제

# people = [
#     ("Blake Howell", "Jamaica", 18, "aw@jul.bw"),
#     ("Peter Bowen", "Burundi", 30, "vinaf@rilkov.il"),
#     ("Winnie Hall", "Palestinian Territories", 22, "moci@pacivhe.net"),
#     ("Alfred Schwartz", "Syria", 29, "ic@tolseuc.pr"),
#     ("Carrie Palmer", "Mauritius", 28, "fenlofi@tor.aq"),
#     ("Rose Tyler", "Martinique", 17, "as@forebjab.et"),
#     ("Katharine Little", "Anguilla", 29, "am@kifez.et"),
#     ("Brent Peterson", "Svalbard & Jan Mayen", 22, "le@wekciga.lr"),
#     ("Lydia Thornton", "Puerto Rico", 19, "lefvoru@itbewuk.at"),
#     ("Richard Newton", "Pitcairn Islands", 17, "da@lasowiwa.su"),
#     ("Eric Townsend", "Svalbard & Jan Mayen", 22, "jijer@cipzo.gp"),
#     ("Trevor Hines", "Dominican Republic", 15, "ev@hivew.tm"),
#     ("Inez Little", "Namibia", 26, "meewi@mirha.ye"),
#     ("Lloyd Aguilar", "Swaziland", 16, "oza@emneme.bb"),
#     ("Erik Lane", "Turkey", 30, "efumazza@va.hn"),
# ]

# # some code

# print(people)

# """
# [('Winnie Hall', 'Palestinian Territories', 22, 'moci@pacivhe.net'),
#  ('Brent Peterson', 'Svalbard & Jan Mayen', 22, 'le@wekciga.lr'),
#  ('Eric Townsend', 'Svalbard & Jan Mayen', 22, 'jijer@cipzo.gp'),
#  ('Inez Little', 'Namibia', 26, 'meewi@mirha.ye'),
#  ('Carrie Palmer', 'Mauritius', 28, 'fenlofi@tor.aq'),
#  ('Alfred Schwartz', 'Syria', 29, 'ic@tolseuc.pr'),
#  ('Katharine Little', 'Anguilla', 29, 'am@kifez.et'),
#  ('Peter Bowen', 'Burundi', 30, 'vinaf@rilkov.il'),
#  ('Erik Lane', 'Turkey', 30, 'efumazza@va.hn')]
# """

from pprint import pprint
people = [
    ("Blake Howell", "Jamaica", 18, "aw@jul.bw"),
    ("Peter Bowen", "Burundi", 30, "vinaf@rilkov.il"),
    ("Winnie Hall", "Palestinian Territories", 22, "moci@pacivhe.net"),
    ("Alfred Schwartz", "Syria", 29, "ic@tolseuc.pr"),
    ("Carrie Palmer", "Mauritius", 28, "fenlofi@tor.aq"),
    ("Rose Tyler", "Martinique", 17, "as@forebjab.et"),
    ("Katharine Little", "Anguilla", 29, "am@kifez.et"),
    ("Brent Peterson", "Svalbard & Jan Mayen", 22, "le@wekciga.lr"),
    ("Lydia Thornton", "Puerto Rico", 19, "lefvoru@itbewuk.at"),
    ("Richard Newton", "Pitcairn Islands", 17, "da@lasowiwa.su"),
    ("Eric Townsend", "Svalbard & Jan Mayen", 22, "jijer@cipzo.gp"),
    ("Trevor Hines", "Dominican Republic", 15, "ev@hivew.tm"),
    ("Inez Little", "Namibia", 26, "meewi@mirha.ye"),
    ("Lloyd Aguilar", "Swaziland", 16, "oza@emneme.bb"),
    ("Erik Lane", "Turkey", 30, "efumazza@va.hn"),
]

# print(people[0][2])
# print(people[1][2])
# print(people[2][2])
# print(people[3][2])

# people_com = []

# for i in range(len(people)):
#     if int(people[i][2]) > 20:
#         people_com.append(people[i])

# pprint(people_com)

# people_comprehension = [x for x in range(len(people)) if int(people[x][2])>20]
# pprint(people_comprehension)

people_filter = list(filter(lambda x : x[2]>20, people))
pprint(people_filter)


    
    
    
    
    