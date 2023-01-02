abcd = "abcd"
reverse_abcd = ''

for i in abcd:
    reverse_abcd = i + reverse_abcd
    
print(reverse_abcd)

abcd_list = list(abcd)
abcd_list.reverse()
abcd_2 = ''.join(abcd_list)
print(abcd_2)

abcd1 = abcd[::1]
abcd2 = abcd[::2]
abcd3 = abcd[::-1]
abcd4 = abcd[::-2]

print(abcd1)
print(abcd2)
print(abcd3)
print(abcd4)


for item in abcd_list[::-1]:
    print(item)