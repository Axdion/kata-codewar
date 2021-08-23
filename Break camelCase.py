#Complete the solution so that the function will break up camel casing, using a space between words.
import string
def solution(s:str):
    word = ''
    w = ''
    for char in s:
        if char in string.ascii_uppercase:
            word = word +w+' '
            w = char
        else:
            w = w+char
    return word+w

print(solution('breakCamelCaseGola'))
