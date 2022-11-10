def solution(s):
    answer = 0
    num_eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num_num_num = ['one', '1', 'two', '2', '3', 'three', '4', 'four', '5', 'five', '6', 'six', '7', 'seven', '8', 'eight', '9', 'nine', 'zero', '0']
    new_num = []


    for i in num_num_num:
        if i in s:
            if i == 'zero':
                new_num.append('0')
            elif i == 'one':
                new_num.append('1')
            elif i == 'two':
                new_num.append('2')
            elif i == 'three':
                new_num.append('3')
            elif i == 'four':
                new_num.append('4')
            elif i == 'five':
                new_num.append('5')
            elif i == 'six':
                new_num.append('6')
            elif i == 'seven':
                new_num.append('7')
            elif i == 'eight':
                new_num.append('8')
            elif i == 'nine':
                new_num.append('9')
            new_num.append(i)

    print(new_num)

    new_new_num = []

    for i in new_num:
        if i in num_num:
            if i == '0':
                new_new_num.append('0')
            elif i == '1':
                new_new_num.append('1')
            elif i == '2':
                new_new_num.append('2')
            elif i == '3':
                new_new_num.append('3')
            elif i == '4':
                new_new_num.append('4')
            elif i == '5':
                new_new_num.append('5')
            elif i == '6':
                new_new_num.append('6')
            elif i == '7':
                new_new_num.append('7')
            elif i == '8':
                new_new_num.append('8')
            elif i == '9':
                new_new_num.append('9')
    
    print(new_new_num)

    number = "".join(new_new_num)

    print(number)

    answer=int(number)

    return answer

solution('one4seveneight')
solution('2three45sixseven')
solution('23four5six7')


    # for i in num_num:
    #     if i in s:
    #         new_num.append(i)

    # for j in num_eng:
    #     if j in s:
    #         if j == 'zero':
    #             new_num.append('0')
    #         elif j == 'one':
    #             new_num.append('1')
    #         elif j == 'two':
    #             new_num.append('2')
    #         elif j == 'three':
    #             new_num.append('3')
    #         elif j == 'four':
    #             new_num.append('4')
    #         elif j == 'five':
    #             new_num.append('5')
    #         elif j == 'six':
    #             new_num.append('6')
    #         elif j == 'seven':
    #             new_num.append('7')
    #         elif j == 'eight':
    #             new_num.append('8')
    #         elif j == 'nine':
    #             new_num.append('9')
    

    # for i in s:
    #     if i in num_num:
    #         new_num.append(i)

    # for j in num_eng:
    #     if j in s:
    #         if j == 'zero':
    #             new_num.append('0')
    #         elif j == 'one':
    #             new_num.append('1')
    #         elif j == 'two':
    #             new_num.append('2')
    #         elif j == 'three':
    #             new_num.append('3')
    #         elif j == 'four':
    #             new_num.append('4')
    #         elif j == 'five':
    #             new_num.append('5')
    #         elif j == 'six':
    #             new_num.append('6')
    #         elif j == 'seven':
    #             new_num.append('7')
    #         elif j == 'eight':
    #             new_num.append('8')
    #         elif j == 'nine':
    #             new_num.append('9')
    
# a = 'zero'
# print(a[0])
# for i in a:
#     print(a[i])