import re

ROMAN_NUMBERS = (('I',1),('V',5),('X',10),('L',50))

def roman_to_integer(value):
    total = 0

    if 'I' in value:
        pattern = '.*I[V,X,L]+'
        if re.match(pattern,value):
            total = total - 1;
            #remove I from string
            value = value.replace("I", "")
    for c in value:
         for item in ROMAN_NUMBERS:
             if item[0] == c:
                 total += item[1]
    return total
