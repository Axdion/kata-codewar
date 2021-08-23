''' Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.'''


def parse(data:str):
    value = 0
    result = []
    for char in data:
        if char == 'i':
            value+=1
        elif char == 'd':
            value-=1
        elif char == 's':
            value *=value
        elif char == 'o':
            result.append(value)
    return result



print(parse('isoisoiso'))
