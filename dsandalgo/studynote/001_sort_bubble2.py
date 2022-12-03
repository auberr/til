num = "2 1 3 8 5 4 7"
nums = num.split()
num_list= []
num_list = [int(i) for i in nums]
cnt = len(num_list)
print(num_list)
print(cnt)

for i in range(0, cnt, 1):
    for j in range(0, cnt-i-1, 1):
        if num_list[j]>num_list[j+1]:
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp
    
print(num_list)

for i in range(0, cnt, 1):
    for j in range(0, cnt-i-1, 1):
        if num_list[j]<num_list[j+1]:
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp

print(num_list)


