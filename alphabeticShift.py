# Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

# Example

# For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string inputString

# A non-empty string consisting of lowercase English characters.

# Guaranteed constraints:
# 1 ≤ inputString.length ≤ 1000.

# [output] string

# The resulting string after replacing each of its characters.

def alphabeticShift(inputString):
    input_str = []
    input_str[:0]=inputString
    inc_list = []



    for i in input_str:
        inc_list.append(chr(ord(i) + 1))

    
            

    inc_str = ''.join(inc_list)
    return inc_str.replace('{', 'a')


print('abcdz => ',alphabeticShift('abcdzz'))