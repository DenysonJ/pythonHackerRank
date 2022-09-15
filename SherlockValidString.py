def isValid(s):
    c = set(s)
    lenght = [s.count(i) for i in c]
    len_c = set(lenght)
    print(len_c)
    if len(len_c) == 1:
        return "YES"
    
    maximum = max(len_c)
    minimum = min(len_c)
    print(maximum, minimum)
    
    if (maximum - minimum == 1) and (lenght.count(maximum) == 1 or lenght.count(minimum)== 1 ):
        return "YES"
    
    if lenght.count(minimum) == 1 and minimum == 1:
        len_c.remove(minimum)

    minimum = min(len_c)
 
    if minimum == maximum:
        return "YES"
    
    return "NO"
