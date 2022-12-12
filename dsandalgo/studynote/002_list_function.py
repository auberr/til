# 리스트 관련 함수 정리 (+본인만의 예제) : https://wikidocs.net/14#_11

# 파이썬의 리스트는 어레이로 구현되어 있다.
# 내부적으로 동적 배열을 사용 -> 배열의 길이가 늘어나도 O(1) 의 시간복잡도
# 배열과 링크드 리스트 합친 것


# 1. 리스트에 요소 추가 (append)
a = [1 , 2, 3, 4]
print("a =", a)

a.append(5)
print("a append 5 / ", a)

a.append([6,7])
print("a append [6,7] /", a)

# 2. 리스트 정렬 (sort, sorted)
# sort 는 배열 자체를 정렬
a = [1, 4, 3, 2]
a.sort()
print("a =", a)
print("sort a | a =", a)

# sorted 는 배열 자체를 바꾸지 않음
# 영어 그대로 sort 된 이라고 생각하면 좋을듯

a = [1, 4, 3, 2]
sorted_a = sorted(a)

print("a =", a)
print("sorted a", sorted_a)

a = [('Smith', 45), ('John', 30), ('Paul', 25)]
sorted_a = sorted(a, key = lambda x: x[1])
print(sorted_a)



# 3. 리스트 역순 정렬 reverse
a = [1, 2, 3, 4]
a.reverse()

print("a =", a)
print("reverse a", a)


# 4. index
# index(x) 함수는 리스트에 x 값이 있으면 x 의 인덱스 값을 리턴
a = [1, 2, 3, 4]
print(a.index(3))


# 5. insert
# insert(a, b) 는 리스트의 a번째 위치에 b 를 삽입
a = [1, 2, 3, 4]
a.insert(4, 5)
print(a)

# 6. remove
# remove(x) 는 리스트에서 첫 번째로 나오는 x를 삭제
a= [1, 2, 3, 4, 1, 2, 3, 4]
a.remove(4)
print(a)
a.remove(4)
print(a)

# 7. pop
# pop 은 리스트의 맨 마지막 요소를 리턴하고 그 요소를 삭제
a = [1, 2, 3, 4]
print(a.pop())
print(a)

# 8. count
# 리스트 안에 x 가 몇개 있는지 개수를 리턴
a = [1, 2, 3, 4, 1, 2, 3, 4]
a.count(1)
print(a)

# 9. extend
# extend(x) 에서 x에는 리스트만 올 수 있다 원래의 리스트에 리스트를 병합

a = [1, 2, 3, 4]
a.extend([5, 6])
print(a)


# 정수 배열일때 max, min

a = [1, 2, 3, 4]
print(max(a))
print(min(a))

# Extended Slices 
# arr[A:B:C]
arr = list(range(10))
print(arr[:2])
print(arr[0:2])
print(arr[::2])


# 스택과 큐
# Stack : 쌓인것 (Last In First Out)
# Quene : 줄 (First In First Out)


# deque 는 python 에서 동시에 되는 것
from collections import deque
queue = deque()


# append # 오른쪽에서 데이터 추가
queue.append(3) # deque([3])
queue.append(5) # deque([3, 5])
queue.append(7) # deque([3, 5, 7])

# pop 오른쪽에서 데이터 삭제
queue.pop()
queue.pop()
