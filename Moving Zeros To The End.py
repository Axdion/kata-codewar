import jedi

'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''

def move_zeros(array:list):
    c = 0
    array1 = []
    for i in array:
        if i ==0:
            c = c+1
        else:
            array1.append(i)
    return array1+[0 for i in range(c)]


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
