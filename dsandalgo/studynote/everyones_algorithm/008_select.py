
def select_sort(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        print(min_idx, '--')
        for j in range(i+1, n):
            print(j, '----')
            if a[j] < a[min_idx]:
                print(i, min_idx, j)
                print('실제수', a[i], a[min_idx], a[j])
                min_idx = j
                a[i], a[min_idx] = a[min_idx], a[i]
                min_idx = i

                print(a)
                
                


d=[2, 4, 5, 1, 3]
print(select_sort(d))
print(d)