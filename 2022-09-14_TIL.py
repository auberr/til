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


class Calc():
    def __init__(self):
        pass

    def set_number(self, num1, num2):
        self.num1 = int(num1)
        self.num2 = int(num2)


    def plus(self):
        plus = self.num1 + self.num2
        return plus

    def minus(self):
        minus = self.num1 - self.num2
        return minus

    def multiple(self):
        multiple = self.num1 * self.num2
        return multiple

    def divide(self):
        divide = self.num1 / self.num2
        return divide

        
try:
    a, b = map(int, input("연산할 두 수를 띄어쓰기로 입력하세요").split())
    calc = Calc()
    calc.set_number(a, b)
    calc.divide()
except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다.")
except NameError:
    print("숫자만 입력 가능합니다.")
else:
    calc = Calc()
    calc.set_number(a, b)
    print(f"더한값은 {calc.plus()} 입니다.")
    print(f"뺀 값은 {calc.minus()} 입니다.")
    print(f"곱한 값은 {calc.multiple()} 입니다.")
    print(f"나눈 값은 {calc.divide()} 입니다.")



    
    
    
    
    