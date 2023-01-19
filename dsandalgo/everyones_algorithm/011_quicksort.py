def quick_sort_sub(a, start, end):
    if end - start <= 0:
        return
    
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]


def quick_sort(a):
    n = len(a)
    if n <= 1:
        return
    pivot = a[-1]
    g1 = []
    g2 = []
    print(pivot)
    for i in range(0, n-1):
        if a[i] < pivot:
            g1.append(a[i])
            print(a[i])
        else:
            g2.append(a[i])
            print(a[i], 'else')
    print(d)

    return quick_sort(g1) + [pivot] + quick_sort(g2)

d = [3, 1, 2, 4]
print(quick_sort(d))