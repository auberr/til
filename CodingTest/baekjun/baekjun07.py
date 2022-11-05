# 2869 번
A, B, V = map(int, input().split())

day=0

if A - B <= 1:
    day = V - A + 1
else:
    day = V // (A -B) + 1
    # while True:
    #     if V > 0:
    #         day +=1
    #         V -= A
    #         if V < 0:
    #             break
    #         elif V >0:
    #             V += B
    #     else:
    #         break

print(day)


# # 1193 번
# N = int(input())

# a = N // 2

# if N % 2 ==0 :
#     b = 0
# elif N % 2 == 1 :
#     b = 1

# print(f"{a}/{b}")

# 10757 번
# A, B = map(int, input().split())

# print(A+B)




# 1712 번

# a, b, c = map(int, input().split())

# if (c - b) <= 0 :
#     i = -1
# else:
#     i = a//(c-b)+1

# print(i)