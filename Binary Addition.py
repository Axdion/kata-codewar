'''
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:

add_binary(1, 1) == "10" (1 + 1 = 2 in decimal or 10 in binary)
add_binary(5, 9) == "1110" (5 + 9 = 14 in decimal or 1110 in binary)
'''


def add_binary(a:int, b:int):
    binary = ''
    n = a + b
    while n !=0:
        binary =   str(n%2) + binary
        n = n//2
    return binary
