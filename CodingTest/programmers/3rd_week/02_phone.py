def solution(phone_number):
    answer = ''
    phone_number_rev = "".join(reversed(phone_number))
    rev_list = list(phone_number_rev)
    
    for i in range(len(phone_number_rev)):
        print(rev_list)
        if i > 3:
            rev_list[i] = '*'
        print(rev_list)
            
    print(rev_list)
    phone_number_rev = ''.join(rev_list)
    phone_number = "".join(reversed(phone_number_rev))
    answer=phone_number
        
    return answer

solution('01033334444')
