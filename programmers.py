def solution(s):
    answer = True
    k= s.lower()
    if k.count('p') == k.count('y'):
        return True
    elif k.count('p')==0 and k.count('y')==0:
        return True
    else:
        False
print(solution("pPoooyY"))