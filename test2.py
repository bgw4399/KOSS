def sol(s):
    stack = [s[0]]
    answer = -1
    for i in range(1, len(s)):
        if len(stack) > 0 and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    return answer
print(sol("baabaa"))