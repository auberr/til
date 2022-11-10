# 11399 
n = int(input())
b = list(map(int, input().split()))

orders = []
for i in range(len(b)):
    k = len(b) - i
    for j in range(1, k):
        if b[j-1] >= b[j]:
            temp = b[j-1]
            b[j-1] = b[j]
            b[j] = temp

sum = 0
new_sum = []
for i in b:
    sum +=i
    new_sum.append(sum)
print(sum)
print(new_sum)

total = 0
for i in new_sum:
    total+=i

print(total)

        

# a = int(input())
# b = list(input())

# c = 0
# for i in range(a):
#     c+=int(b[i])

# print(c)