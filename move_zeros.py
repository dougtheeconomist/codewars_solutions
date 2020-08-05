import numpy as np

def move_zeros(array):
    '''
    Write an algorithm that takes an array and moves all of the zeros to the end, 
    preserving the order of the other elements.
    '''
    step = [num for num in array]
    count = [i for i in range(len(step)-1,-1,-1)]
    
    for i in count:
        if step[i] is False:
            pass

        elif step[i] == 0:
            step.append(step.pop(i))

    return step

testcase = np.array([[1,2,0,1,0],[1,0,3,0,-1]])

# print(move_zeros(testcase))
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))