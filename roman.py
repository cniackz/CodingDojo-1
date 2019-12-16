import re

def roman_to_integer(value):
    number_dict = {'I':1, "V":5, "X":10, "L":50}
    total = 0
    i_sum = value.count("I")
    v_sum = value.count("V")

    if 'I' in value:
        pattern = '.*I[V,X,L]+'
        if re.match(pattern,value):
            total = total - 1;
            #remove I from string
            value = value.replace("I", "")
    for c in value:
         total += number_dict[c]
    return total
