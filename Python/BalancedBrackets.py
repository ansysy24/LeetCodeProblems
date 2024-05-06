def balancedBrackets(string):
    stack = []
    inverted = {')': '(', ']': '[', '}': '{'}
    for ch in string:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if stack and stack[-1] == inverted[ch]:
                stack.pop()
            else:
                return False
    return stack == []

print(balancedBrackets('(((((([[[[[[{{{{{{{{{{{{()}}}}}}}}}}}}]]]]]]))))))((([])({})[])[])[]([]){}(())'))