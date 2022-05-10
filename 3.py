def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        k = 0
        for j in range(2, i):
            if i % j == 0:
                k += 1
        if k % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
print(solution(13,17))