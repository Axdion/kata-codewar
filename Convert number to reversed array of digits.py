''' Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]'''


def digitize(n):
    array = []
    while n!=0:
        #Digit extract
        array.append(n%10)
        n = n // 10
    return array



print(digitize(1997))
