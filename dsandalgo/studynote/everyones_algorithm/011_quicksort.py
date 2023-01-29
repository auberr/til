def quick_sort_sub(a, start, end):
    if end - start <= 0:
        return
    
    pivot = a[end]
    print(pivot, '피봇')
    i = start
    print(i, '스타트')
    for j in range(start, end):
        if a[j] <= pivot:
            print(a[i], a[j], '--------')
            a[i], a[j] = a[j], a[i]
            print(a[i], a[j], '----')
            i+=1
            print(a, 'a입나다')
    a[i], a[end] = a[end], a[i]
    print(a[i], "스타트", a[end], "엔드")
    quick_sort_sub(a, start, i - 1)
    quick_sort_sub(a, i+1, end)
    
def quick_sort(a):
    quick_sort_sub(a, 0, len(a)-1)

d = [6,8,3,9]
quick_sort(d)
print(d)


# def quick_sort(a):
#     n = len(a)
#     if n <= 1:
#         return
#     pivot = a[-1]
#     g1 = []
#     g2 = []
#     print(pivot)
#     for i in range(0, n-1):
#         if a[i] < pivot:
#             g1.append(a[i])
#             print(a[i])
#         else:
#             g2.append(a[i])
#             print(a[i], 'else')
#     print(d)

#     return quick_sort(g1) + [pivot] + quick_sort(g2)

# d = [3, 1, 2, 4]
# print(quick_sort(d))



def bubble_sort(a):
    n = len(a)
    while True:
        changed = False
        for i in range(0, n-1):
            if a[i] > a[i+1]:
                print(a)
                a[i], a[i+1] = a[i +1], a[i]
                changed = True
        if changed == False:
            return

d = [2, 4, 5, 1, 3]
bubble_sort(d)
print(d)
        