# 1316




#2941 
# croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

# user_input = input()

# for i in croatia:
#      user_input = user_input.replace(i, '*')

# print(len(user_input))

#      if user_input_list[i] in croatia:
#           count+=1

# print(count)



#5622
# alphabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# word = input()

# time = 0
# for unit in alphabet_list:
#      for i in unit: # 알파벳 리스트에서 각 요소를 꺼내서 한글자씩 분리
#           for x in word: # 입력받은 문자를 하나씩 분리
#                if i == x: # 두 알파벳이 같으면
#                     time +=alphabet_list.index(unit) +3

# print(time)


# check_alphabet = [{"ABC":2},{"DEF":3},{"GHI":4},{"JKL":5},{"MNO":6},{"PQRS":7},{"TUV":8},{"WXYZ":9}]

# user_input = input().split()
# user_input_list =[]

# for i in user_input:
#      user_input_list +=i
#      if user_input_list[i] in check_alphabet[i]:
#           print(check_alphabet)

# print(user_input_list)

# 2908

# A, B = map(int, input().split())

# sang_A = str(A)[::-1]
# sang_B = str(B)[::-1]

# sang_num_A = int(sang_A)
# sang_num_B = int(sang_B)

# if sang_num_A > sang_num_B:
#      print(sang_num_A)
# else :
#      print(sang_num_B)

# 1152

# words = input().split()

# print(len(words))


# # #1157

# new_word = input()
# word_manufactured = new_word.upper()

# a = word_manufactured.count('A')
# b = word_manufactured.count('B')
# c = word_manufactured.count('C')
# d = word_manufactured.count('D')
# e = word_manufactured.count('E')
# f = word_manufactured.count('F')
# g = word_manufactured.count('G')
# h = word_manufactured.count('H')
# i = word_manufactured.count('I')
# j = word_manufactured.count('J')
# k = word_manufactured.count('K')
# l = word_manufactured.count('L')
# m = word_manufactured.count('M')
# n = word_manufactured.count('N')
# o = word_manufactured.count('O')
# p = word_manufactured.count('P')
# q = word_manufactured.count('Q')
# r = word_manufactured.count('R')
# s = word_manufactured.count('S')
# t = word_manufactured.count('T')
# u = word_manufactured.count('U')
# v = word_manufactured.count('V')
# w = word_manufactured.count('W')
# x = word_manufactured.count('X')
# y = word_manufactured.count('Y')
# z = word_manufactured.count('Z')

# check_list = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]


# big = 0
# question ="?"
# select = ""

# for i in range(len(check_list)):
#      if check_list[i] > int(big):
#           big = check_list[i]
#           select = check_list[i]
          

#      elif check_list[i] == int(big):
#           big = 11111


# if big == 11111:
#      big = question

# print(big)
# print(select)


# # for i in check_list:
# #      if i > :
# #           i = check_list[i]

# ############2675

# T = int(input())

# for i in range(T):
#      num, word = input().split()
#      text= ''
#      for i in word:
#           text += int(num) * i
#      print(text)



# T = int(input())

# S = input()

# for _ in range(T):
#      S_list = list(S)

#      for i in S_list:
#           while i <T:
#                print(S_list)[i]
     


#10809

# word = list(input())
# c = 'abcdefghijklmnopqrstuvwxyz'

# for i in c:
#      if i in word:
#           print(S.index(i), end=' ')
#      else:
#           print(-1, end='')

# word = list(input())

# if 'a' in word:
#      print(str(word.index('a'))+' ', end='')
# elif 'a' not in word:
#      print('-1 ', end='')

# if 'b' in word:
#      print(str(word.index('b'))+' ', end='')
# elif 'b' not in word:
#      print('-1 ', end='')


# if 'c' in word:
#      print(str(word.index('c'))+' ', end='')
# elif 'c' not in word:
#      print('-1 ', end='')


# if 'd' in word:
#      print(str(word.index('d'))+' ', end='')
# elif 'd' not in word:
#      print('-1 ', end='')


# if 'e' in word:
#      print(str(word.index('e'))+' ', end='')
# elif 'e' not in word:
#      print('-1 ', end='')


# if 'f' in word:
#      print(str(word.index('f'))+' ', end='')
# elif 'f' not in word:
#      print('-1 ', end='')

# if 'g' in word:
#      print(str(word.index('g'))+' ', end='')
# elif 'g' not in word:
#      print('-1 ', end='')

# if 'h' in word:
#      print(str(word.index('h'))+' ', end='')
# elif 'h' not in word:
#      print('-1 ', end='')

# if 'i' in word:
#      print(str(word.index('i'))+' ', end='')
# elif 'i' not in word:
#      print('-1 ', end='')

# if 'j' in word:
#      print(str(word.index('j'))+' ', end='')
# elif 'j' not in word:
#      print('-1 ', end='')

# if 'k' in word:
#      print(str(word.index('k'))+' ', end='')
# elif 'k' not in word:
#      print('-1 ', end='')

# if 'l' in word:
#      print(str(word.index('l'))+' ', end='')
# elif 'l' not in word:
#      print('-1 ', end='')

# if 'm' in word:
#      print(str(word.index('m'))+' ', end='')
# elif 'm' not in word:
#      print('-1 ', end='')

# if 'n' in word:
#      print(str(word.index('n'))+' ', end='')
# elif 'n' not in word:
#      print('-1 ', end='')

# if 'o' in word:
#      print(str(word.index('o'))+' ', end='')
# elif 'o' not in word:
#      print('-1 ', end='')

# if 'p' in word:
#      print(str(word.index('p'))+' ', end='')
# elif 'p' not in word:
#      print('-1 ', end='')

# if 'q' in word:
#      print(str(word.index('q'))+' ', end='')
# elif 'q' not in word:
#      print('-1 ', end='')

# if 'r' in word:
#      print(str(word.index('r'))+' ', end='')
# elif 'r' not in word:
#      print('-1 ', end='')

# if 's' in word:
#      print(str(word.index('s'))+' ', end='')
# elif 's' not in word:
#      print('-1 ', end='')

# if 't' in word:
#      print(str(word.index('t'))+' ', end='')
# elif 't' not in word:
#      print('-1 ', end='')

# if 'u' in word:
#      print(str(word.index('u'))+' ', end='')
# elif 'u' not in word:
#      print('-1 ', end='')

# if 'v' in word:
#      print(str(word.index('v'))+' ', end='')
# elif 'v' not in word:
#      print('-1 ', end='')

# if 'w' in word:
#      print(str(word.index('w'))+' ', end='')
# elif 'w' not in word:
#      print('-1 ', end='')

# if 'x' in word:
#      print(str(word.index('x'))+' ', end='')
# elif 'x' not in word:
#      print('-1 ', end='')

# if 'y' in word:
#      print(str(word.index('y'))+' ', end='')
# elif 'y' not in word:
#      print('-1 ', end='')

# if 'z' in word:
#      print(str(word.index('z')), end='')
# elif 'z' not in word:
#      print(-1)


# #11720 

# N = int(input())
# num = list(input())
# sum = 0

# # print(type(num))
# # print(num)

# for i in num:
#      sum += int(i)

# print(sum)

#11654

# a = input()

# if type(a) == int:
#      print(chr(a))
# elif type(a) == str:
#      print(ord(a))

# a = chr(a)

# print(a)