t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    s=input()
    max_x=max_y=max_xy=max_nxy=min_x=min_y=min_xy=min_nxy=0
    for ch in s:
        if ch=='4':
            max_x+=1
            max_y+=1
            max_xy+=1
            max_nxy+=1
            min_x-=1
            min_y-=1
            min_x-=1
            min_xy-=1
            min_nxy-=1
        else:
                max_x+=1
                max_y+=1
                max_xy+=2
                max_nxy+=2
                min_x-=1
                min_y-=1
                min_x-=1
                min_xy-=2
                min_nxy-=2
    if(min_x<=x<=max_x and min_y<=y<=max_y and
        min_xy<=x+y<=max_xy and min_nxy<=x-y<=max_nxy
       ):
         print("YES")
    else:
         print("NO")
                

            
