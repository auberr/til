#GCD (Greatest Common Divisor)
#LCM (Least Common Multiple)
# https://codingpractices.tistory.com/entry/Python-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EB%9E%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0
# https://codingpractices.tistory.com/46


import random

a = random.randint(1, 99)
b = random.randint(1, 99)

for i in range(min(a, b), 0, -1):
    if a%i ==0 and b%i ==0:
        print(i)
        break
    
for i in range(max(a, b), (a*b)+1):
    if i % a ==0 and i % b == 0:
        print(i)
        break

for i in range(b, a*b+1):
    if i%a == 0 and i % b ==0:
        print(i)
        break
    
def LCM(a, b):
    if a <b :
        max = b
    elif a >b:
        max = a
    for i in range(max, a*b+1):
        if i % a == 0 and i % b ==0:
            res = i
            break
    return res

print(LCM(a, b))
        


list_gcd_4 =[]


def UC_gcd(a, b):
    while(b):
        a, b = b, b%a
    return a

def gcd_4(a, b):
    if a < b:
        min = a
    else : 
        min = b 
    for i in range(min+1, 0, -1):
        if a % i == 0 and b % i == 0:
            list_gcd_4.append(i)
    
    return list_gcd_4[0]

print(gcd_4(a, b))


def gcd_3(a, b):
    while a * b !=0:
        if b >= a:
            if b % a == 0:
                x = a
                break
            else:
                b = b % a
        else:
            if a % b == 0:
                x = b
                break
            else:
                a = a % b
    return x


a = random.randint(1, 99)
b = random.randint(1, 99)

div_2 = []

def gcd_2(a, b):
    if a > b:
        for i in range(1, b+1):
            if b % i == 0:
                if a % i == 0:
                    div_2.append(i)
    
    else:
        for i in range(1, a+1):
            if a % i == 0:
                if b % i == 0:
                    div_2.append(i)
    
    return div_2[-1]

print(gcd_2(a, b))          



list_a = []
list_b = []
a = random.randint(1, 99)
b = random.randint(1, 99)

div = []

def gcd(a, b):
    for i in range(1, a+1):
        if a % i == 0:
            list_a.append(i)
    
    for i in range(1, b+1):
        if b % i == 0:
            list_b.append(i)
    
    for i in range(len(list_a)):
        for j in range(len(list_b)):
            if list_a[i] == list_b[j]:
                div.append(list_a[i])
                
     
    return div[-1]

print(gcd(a, b))          




list_1=[]

a = random.randint(1, 99)

def divsors(a):
    for i in range(1, a+1):
        if a % i == 0:
            list_1.append(i)
    return list_1

print(divsors(a))



# def cd(a, b):
    