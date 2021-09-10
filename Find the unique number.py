'''There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique '''

def find_uniq(arr:list):
    if len(arr)==1:
        return arr[0]
    else:
        if arr.count(arr[0])>1:
            return find_uniq([x for x in arr if x != arr[0]])
        else:
            return arr[0]
#Al usarse recursividad, la complejidad del algoritmo baja considerablemente
#lo que permite tener un algoritmo efectivo en caso de listas de gran longitud
