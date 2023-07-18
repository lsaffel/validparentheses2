def validparentheses(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "{" or s[i] == "[":
            # print("s[i] is ", s[i])
            stack.append(s[i])
            # print("stack currently is: ", stack)
        else:
            if stack:   # if the stack is not empty
                prevCh = stack.pop()
                # print("prevCh is: ", prevCh)

            else:       # the stack is empty
                return False
            if matchingPair(s[i], prevCh) == False:
                return False
    # if the remaining stack is not empty, then the string is not a valid set of parentheses
    if stack:   # stack is non-empty
        return False
    else:       # the stack is empty
        return True

# def checkChOK(ch, stack):
#     if ch == "(" or ch == "{" or ch == "[":
#         stack.append(ch)
#         return True
#     else:
#         if stack:
#             nextCh = stack.pop()
#         else:
#             return False
#         return matchingPair(ch, nextCh)

def matchingPair(ch, prevCh):
    if (ch == "]" and prevCh == "[") or (ch == "}" and prevCh == "{") or (ch == ")" and prevCh == "("):
        return True
    else:
        return False
