def med3_1(a, b, c):
    if a>= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else: 
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else: 
        return b


def med3(a, b, c):
    med =0
    if a > b:
        if b > c:
            med = b
        elif c > b:
            if a > c:
                med = a
            elif a < c:
                med = c
    elif b > a:
        if a > c:
            med = a
        elif a < c:
            if b > c:
                med = c
            elif b < c:
                med = b
    return med

print(med3(3, 5, 7))