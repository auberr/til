# ## 1. 도형 넓이 계산기

# ### 요구조건

# - 인스턴스를 선언할 때 가로, 세로 길이를 받을 수 있는 클래스를 선언해 주세요
# - 인스턴스에서 사각형, 삼각형, 원의 넓이를 구하는 메소드를 생성해주세요
#     - 원의 넓이를 계산할 때는 세로 길이는 무시하고, 가로 길이를 원의 지름이라 가정하고 계산해 주세요

import math

math.pi

class Area():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        self.square_area = self.width * self.height
        return self.square_area

    def triangle(self):
        self.triangle_area = self.width * self.height / 2
        return self.triangle_area

    def circle(self):
        self.circle_area = self.width/2 * self.width/2 * math.pi
        return self.circle_area

area = Area(10, 20)
print(area.square())
print(area.triangle())
print(area.circle())

# 참고 블로그 :
# [보고의 진땀나는 하루:티스토리] [Python] - 원주율 pi(π), 모듈에서 가져다 쓰기
# https://generalbulldog.tistory.com/21

