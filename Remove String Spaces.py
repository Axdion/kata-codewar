#Simple, remove the spaces from the string, then return the resultant string.
def no_space(x:str):
    return ''.join([w for w in x if w!=' '])


print(no_space('Hola mundo desde Atom'))
