def descending_order(num):
    # Bust a move right here
    numstring=str(num)
    place = [char for char in numstring]
    place.sort(reverse=True)
    out=''
    for i in place:
        out += i

    return int(out)

test1=526182903
print(descending_order(test1))

# def split(word): 
#     return [char for char in word]  

#OTHER CODE THAT IS MUCH MORE CONCISE THAN MINE
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
