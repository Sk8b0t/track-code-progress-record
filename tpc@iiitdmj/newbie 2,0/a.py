t=int(input())
while t:
    x,k=map(int,input().split())
    y=x
    jod=0
    while True:
        for no in str(y):
            jod+=int(no)
        if jod%k==0:
            print(y)
            break
        y+=1
        jod=0
            
        
    t-=1