# You are given a parentheses sequence, check if it's regular.

# Example

# For s = "()()(())", the output should be
# validParenthesesSequence(s) = true;
# For s = "()()())", the output should be
# validParenthesesSequence(s) = false.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string s

# A string, consisting only of '(' and ')'.


def validParenthesesSequence(s):
    s_list = []
    s_list[:0]=s
    open_paren = 0
    closed_paren = 0

    if (len(s_list) == 0):
        return True

    if (s_list[0] == ')') or (s_list[len(s_list) -1] == '('):
        return False
    
    for i in s_list:
        if (i == '('):
            open_paren = (open_paren + 1)

        if (i == ')'):
            closed_paren = (closed_paren + 1)

    paren_sum = (open_paren - closed_paren)
    if (paren_sum == 0):
        return True
    return False



print('should be false: ', validParenthesesSequence("()()(()))("))
print('should be true: ', validParenthesesSequence(""))
print('should be true: ', validParenthesesSequence("()()(())"))

""