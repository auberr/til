from random import choice

my_list = ["가위", "바위", "보"]
my_select = choice(my_list)

possible_values = ["가위", "바위", "보"]

while True:
    player_value = input("가위, 바위, 보 중에서 내주세요")

    if player_value in possible_values:
        break
    else:
        print("제대로 입력하세요.")


if player_value == "가위":
    if my_select =="바위":
        print("컴퓨터가 바위이니 졌습니다.")
    elif my_select =="보":
        print("컴퓨터가 보이니 이겼습니다.")
    elif my_select=="가위":
        print("컴퓨터가 가위이니 비겼습니다.")

elif player_value == "바위":
    if my_select =="바위":
        print("컴퓨터가 바위이니 비겼습니다.")
    elif my_select =="보":
        print("컴퓨터가 보이니 졌습니다.")
    elif my_select=="가위":
        print("컴퓨터가 가위이니 이겼습니다.")

elif player_value == "보":
    if my_select =="바위":
        print("컴퓨터가 바위이니 이겼습니다.")
    elif my_select =="보":
        print("컴퓨터가 보이니 비겼습니다.")
    elif my_select=="가위":
        print("컴퓨터가 가위이니 졌습니다.")
