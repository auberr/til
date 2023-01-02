# 문자 개수 세기 (count)
a = "hobby"
print(a.count('b'))

# 위치 알려주기1 (find) - 문자열 중 문자 ' ' 가 처음 나온 위치를 반환 / 존재하지 않을 경우에 -1 을 반환
a = "Python is the best choice"
a_find = a.find('b')
print(a_find)

# 위치 알려주기2 (index) - 문자열 중 문자 ' ' 가 처음 나온 위치를 반환 / 존재하지 않을 경우에 오류
a = "Life is too short"
a_t = a.index('t')
print(a_t)
# a_k = a.index('k')
# print(a_k)

# 문자열 삽입 (join)
join_1 = ",".join('abcd')
print(join_1)

join_2 = ",".join(['a', 'b', 'c', 'd'])
print(join_2)

# 소문자를 대문자로 바꾸기(upper)
a = "hi"
a_upper = a.upper()
print(a_upper)

# 대문자를 소문자로 바꾸기 (lower)
a = "HI"
a_lower = a.lower()
print(a_lower)

# 왼쪽 공백 지우기(lstrip)
a = " hi hi "
print(a)
a_lstrip = a.lstrip()
print(a_lstrip)

# 오른쪽 공백 지우기
a_rstrip = a.rstrip()
print(a_rstrip)

a_strip = a.strip()
print(a_strip)

# 문자열 바꾸기 (replace)
a = "Life is too short"
a_replace = a.replace("Life", "Your leg")
print(a_replace)

# str.replace('변경하고 싶은 문자', '변경 후 문자', 횟수)

a_replace_2 = a.replace('i', 'a', 2)
print(a_replace_2)



# 문자열 나누기 (split)
a = "Life is too short"
a_split = a.split()
print(a_split)

b = "a:b:c:d"
b_split = b.split(':')
print(b_split)

# slicing
a = "abcdefg"
print(a[0:1])
print(a[0:2])
print(a[0:3])
print(a[0:len(a)])
print(a[0:len(a)+1])
print(a[0:-1])
print(a[3:-2])
print(a[:-3])
print(a[::-2])
print(a[::-1])
