def digital_root(n):
    '''
    A digital root is the recursive sum of all the digits in a number. 
    Given n, take the sum of the digits of n. 
    If that value has more than one digit, continue reducing in this way 
    until a single-digit number is produced. 
    This is only applicable to the natural numbers.
    '''
    
    if n == 0:
        return 0
    numstring= str(n)
    numlist = [int(char) for char in numstring]
    
    if len(numlist) == 1:
        return numlist[0]
    
    def check_it(lst):
        working = 0
        for i in lst:
            working += i
        wstring = str(working)
        out = [int(char) for char in wstring]
        return out
    
    while len(check_it(numlist)) > 1:
        numlist = check_it(numlist)
        check_it(numlist)
    
    return check_it(numlist)[0]

print(digital_root(0))

