t=int(input())
while t:
    n,k=map(int,input().split())
    s=input().strip()
    freq=[0]*26
    for ch in s:
        freq[ord(ch)-ord('a')]+=1
    cnt=0
    for no in freq:
        if no%2!=0:
            cnt+=1
    if cnt>k+1:
        print("NO")
    else:
        print("YES")
    t-=1