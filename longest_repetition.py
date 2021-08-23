'''
For a given string s find the character c (or C) with longest consecutive repetition and return:

(c, l)
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

For empty string return:

('', 0)
'''


def longest_repetition(chars:str):
    if len(chars)==0:
        return ('', 0)
    letter = chars[0]
    string = ''
    list_separate = []
    for char in chars:
        if letter == char:
            string = string+letter
        else:
            list_separate.append(string)
            letter = char
            string = letter
    list_separate.append(string)
    maximum_length = max([len(x) for x in list_separate])
    list_max = [x for x in list_separate if len(x) == maximum_length]
    return (list_max[0][0],maximum_length)




print(longest_repetition('bbbaaabaaaa'))
