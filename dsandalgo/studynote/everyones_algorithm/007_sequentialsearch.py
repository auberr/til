
# def search_list(a, x):
#     n = len(a)
#     list = []
#     for i in range(0, n):
#         if x == a[i]:
#             list.append(i)
#             return list
#     return list

# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(search_list(v, 18))
# print(search_list(v, 33))
# print(search_list(v, 900))


def student_list(n, stu_no, stu_name):
    for i in range(0,len(stu_no)):
        if n == stu_no[i]:
            return stu_name[i]
    return "?"

print(student_list(14, [39,14,67,105], ["Justin", "John", "Mike", "Summer"]))


def get_name(s_no, s_name, find_no):
    n = len(s_no)
    for i in range(0, n):
        if find_no == s_no[i]:
            return s_name[i]
    return "?"

sample_no = [39, 14, 67, 105]
sample_name = ["Justin", "John", "Mike", "Summer"]

print(get_name(sample_no, sample_name, 39))
print(get_name(sample_no, sample_name, 105))
print(get_name(sample_no, sample_name, 777))

# def seq(n):
#     for i in range(0, len(n)):
#         if n[i] == 3:
#             return i+1
#     return -1


# print(seq([1, 5, 4, 2, 3]))

# def search_list(a, x):
#     n = len(a)
#     for i in range(0, n):
#         if x == a[i]:
#             return i
#     return -1

# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(search_list(v, 18))
# print(search_list(v, 33))
# print(search_list(v, 900))