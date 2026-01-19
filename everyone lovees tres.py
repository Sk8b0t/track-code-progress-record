t=int(input())
for _ in range(t):
    n=int(input())
    s=""
    if n%2==0:
        for i in range(n-2):
            s+="3"
        s+="66"
    else:
        if n>=5:
            for i in range(n-5):
                s+="3"
            s+="36366"
        else:
            s="-1"
    print(s)

