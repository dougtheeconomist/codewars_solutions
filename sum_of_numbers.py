def get_sum(a,b):
    '''Given two integers a and b, which can be positive or negative, 
    find the sum of all the numbers between including them too and return it. 
    If the two numbers are equal return a or b.
    Note: a and b are not ordered!
    '''
    #good luck!
    if a == b:
        return a
    s_list=[a,b]
    s_list.sort()
    mid=[]

    for i in range(s_list[0],(s_list[1]+1)):
        mid.append(i)
    
    return sum(mid)

print(get_sum(-5,-2))

