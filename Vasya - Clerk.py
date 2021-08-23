'''The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO. '''


#Solo hay billetes de 100,50 y 25 dolares
#el boleto cuesta $25

def tickets(people:list):
    cash_box = 0
    for cash in people:
        sub = cash-25
        if sub ==0:
            cash_box +=25
        elif sub > cash_box:
            return 'NO'
        else:
            cash_box = cash_box - sub +25
    return 'YES'
