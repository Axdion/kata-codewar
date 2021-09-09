def rgb(r:int ,g:int ,b:int ):
    return dec_to_hexdec(r)+dec_to_hexdec(g)+dec_to_hexdec(b)


def dec_to_hexdec(number:int):
    hexdecimal = ''
    if number <= 0:
        return '00'
    elif number > 255:
        return 'FF'
    while number !=0:
        digit = number %16
        if digit == 10:
            hexdecimal = 'A'+hexdecimal
        elif digit == 11:
            hexdecimal = 'B'+hexdecimal
        elif digit == 12:
            hexdecimal = 'C'+hexdecimal
        elif digit == 13:
            hexdecimal = 'D'+hexdecimal
        elif digit == 14:
            hexdecimal = 'E'+hexdecimal
        elif digit == 15:
            hexdecimal = 'F'+hexdecimal
        else:
            hexdecimal = str(digit) + hexdecimal
        number = number // 16

    return hexdecimal if len(hexdecimal)==2 else '0'+hexdecimal

print(rgb(0,0,0))
