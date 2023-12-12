# 16937 두 스티커 S3
import sys
input = sys.stdin.readline

h,w = map(int,input().split())
n = int(input())
stk = list(list(map(int,input().split())) for _ in range(n))

result = 0
for i in range(n):
    for j in range(i+1,n):
        r1,c1 = stk[i]
        r2,c2 = stk[j]

        if (r1+r2<=h and max(c1,c2)<=w) or (c1+c2<=w and max(r1,r2)<=h):
            result = max(result,r1*c1 + r2*c2)
        if (r1+c2<=h and max(c1,r2)<=w) or (c1+r2<=w and max(r1,c2)<=h):
            result = max(result,r1*c1 + r2*c2)
        if (c1+r2<=h and max(r1,c2)<=w) or (r1+c2<=w and max(c1,r2)<=h):
            result = max(result,r1*c1 + r2*c2)
        if (c1+c2<=h and max(r1,r2)<=w) or (r1+r2<=w and max(c1,c2)<=h):
            result = max(result,r1*c1 + r2*c2)
print(result)