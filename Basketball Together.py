N, D = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
cnt=total=0
for i in range(1,N+1):
    TM=(D//p[N-i])+1
    total+=TM
    if total<=N:
        cnt+=1
    else:
        break
print(cnt)