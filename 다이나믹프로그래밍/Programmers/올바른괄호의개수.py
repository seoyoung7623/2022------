# 올바른 괄오의 개수 
#1. 값을 저장해 중복을 제거하는 방법
def solution2(n):
    memo = [[],['()']]
    combis = [[]]
    for i in range(1,n+1):
        kinds = []
        for j in range(1,i+1):
            for k in range(1,i-j+1):
                if j+k == i:
                    kinds.append((j,k))
        combis.append(kinds)
        
    for i in range(2,n+1):
        temp = []
        for l in memo[i-1]:
            temp.append('('+l+')')
        for j,k in combis[i]:
            for t1 in memo[j]:
                for t2 in memo[k]:
                    temp.append(t1+t2)
        memo.append(list(set(temp)))
    print(memo)
    return len(memo[n])

#2. 카탈란 수
def solution(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]

print(solution(4))