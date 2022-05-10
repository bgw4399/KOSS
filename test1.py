from itertools import combinations
def solution(nums):
    answer = 0
    k = list(combinations(nums, 3))
    print(k)
    for i in range(len(k)):
        t = sum(k[i])
        for j in range(2,t):
            print(j)
            if t % j == 0:
                break
        else:
            answer += 1

    return answer
print(solution([1,2,3,4]))