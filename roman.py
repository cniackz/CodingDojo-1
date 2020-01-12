import re

ROMAN_NUMBERS = (('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000))

def roman_to_integer(value):
    if isinstance(value,int):
        return -1
    total = 0
    # Compile the paterns prior using it thru the code.
    # The idea is to make this faster and more efficient.
    pattern_1 = re.compile(r".*VX")
    pattern_2 = re.compile(r".*I[V,X,L,C,D,M]+")
    if re.match(pattern_1,value):
        return -1
    if 'I' in value:
        if re.match(pattern_2,value):
            total = total - 1;
            #remove I from string
            value = value.replace("I", "")
    for letter in value:
         for item in ROMAN_NUMBERS:
             if item[0] == letter:
                 total += item[1]
    return total
