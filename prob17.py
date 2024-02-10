def num_lett_count():
    dictionary = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        00: 'hundred',
        1000: 'onethousand',
        'and': 3,
    }

    ones = len(dictionary[1])+len(dictionary[2])+len(dictionary[3])+len(dictionary[4])+len(dictionary[5])+len(dictionary[6])+len(dictionary[7])+len(dictionary[8])+len(dictionary[9])
    # print('ones', ones)
    tens = len(dictionary[10])+len(dictionary[11])+len(dictionary[12])+len(dictionary[13])+len(dictionary[14])+len(dictionary[15])+len(dictionary[16])+len(dictionary[17])+len(dictionary[18])+len(dictionary[19])
    # print('tens', tens)
    twenties = ones+len(dictionary[20])*10
    # print('twenties', twenties)
    thirties = ones+len(dictionary[30])*10
    # print('thirties', thirties)
    forties = ones+len(dictionary[40])*10
    # print('forties', forties)
    fifties = ones+len(dictionary[50])*10
    # print('fifties', fifties)
    sixties = ones+len(dictionary[60])*10
    # print('sixties', sixties)
    seventies = ones+len(dictionary[70])*10
    # print('seventies', seventies)
    eighties = ones+len(dictionary[80])*10
    # print('eighties', eighties)
    nineties = ones+len(dictionary[90])*10
    # print('nineties', nineties)
    decs = ones+tens+twenties+thirties+forties+fifties+sixties+seventies+eighties+nineties
    # print('decs', decs)
    one_hundreds = (len(dictionary[1])+len(dictionary[00]))*100+(dictionary['and']*99)+decs
    # print('100s', one_hundreds)
    two_hundreds = (len(dictionary[2])+len(dictionary[00]))*100+(dictionary['and']*99)+decs
    # print('200s', two_hundreds)
    three_hundreds = (len(dictionary[3])+len(dictionary[00]))*100+(dictionary['and']*99)+decs
    # print('300s', three_hundreds)
    four_hundreds = (len(dictionary[4])+len(dictionary[00]))*100+(dictionary['and']*99)+decs
    # print('400s', four_hundreds)
    five_hundreds = (len(dictionary[5])+len(dictionary[00]))*100+(dictionary['and']*99)+decs
    # print('500s', five_hundreds)
    six_hundreds = (len(dictionary[6])+len(dictionary[00]))*100+(dictionary['and']*99)+decs
    # print('600s', six_hundreds)
    seven_hundreds = (len(dictionary[7])+len(dictionary[00]))*100+(dictionary['and']*99)+decs
    # print('700s', seven_hundreds)
    eight_hundreds = (len(dictionary[8])+len(dictionary[00]))*100+(dictionary['and']*99)+decs
    # print('800s', eight_hundreds)
    nine_hundreds = (len(dictionary[9])+len(dictionary[00]))*100+(dictionary['and']*99)+decs
    # print('900s', nine_hundreds)
    hundreds = one_hundreds+two_hundreds+three_hundreds+four_hundreds+five_hundreds+six_hundreds+seven_hundreds+eight_hundreds+nine_hundreds
    # print('hundreds', hundreds)

    return decs+hundreds+len(dictionary[1000])

print('The answer is', num_lett_count())