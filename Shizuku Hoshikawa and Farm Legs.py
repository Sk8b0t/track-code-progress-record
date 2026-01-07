t=int(input())
for i in range(t):
    n=int(input())
    cnt=0
    if n%4==0 :
        chickens=n//2
        cows=0
        if chickens!=1:
            while(chickens!=0):
                
                chickens-=2
                cows+=1
                cnt+=1
            cnt+=1
        
    elif n%2==0:
        chickens=n//2
        cows=0
        if chickens!=1:
            while(chickens!=1):
                
                chickens-=2
                cows+=1
                cnt+=1
        cnt+=1
        
        
    
    print(cnt)
