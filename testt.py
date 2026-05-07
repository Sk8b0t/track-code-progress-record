t=int(input())
while t:
    s=input()
    zero=s.count('0')
    one=s.count('1')
    k=""
    cnt=0
    if zero==one:
        print(0)
    else:
        for i in range(len(s)):
            if s[i]=='0':
                if one>0:
                 one-=1
                else:
                    cnt=i
                    break
            else:
                if zero>0:
                 zero-=1
                else:
                    cnt=i
                    break
        print(len(s)-cnt)
        
    t-=1