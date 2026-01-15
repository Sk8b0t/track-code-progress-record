t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    kcnt=cnt=0
    dup=-1
    for item in a :
        if item ==k:
            kcnt+=1
        if item<k:
            if dup!=item:
                cnt+=1
                dup=item
    print(max(k-cnt,kcnt))

