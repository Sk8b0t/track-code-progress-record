z=int(input())
while z:
    s=input()
    zero=one=0
    for i in s:
        if i=='1':
            one+=1
        else:
            zero+=1 

    can_match_until=0
    if zero==one:
        print(0)
    else:

        for i in range(len(s)+1):
            if s[i]=='1':
                if zero>0:
                    zero-=1
                else:
                    can_match_until=i
                    break
            else:
                if one>0:
                    one-=1
                else:
                    can_match_until=i
                    break
        print(len(s)-can_match_until)
    z-=1


# for _ in range(int(input())):
#     s = input()
#     cnt = [0, 0]
#     for i in range(len(s)):
#         cnt[int(s[i])] += 1
#     for i in range(len(s) + 1):
#         if (i == len(s) or cnt[1 - int(s[i])] == 0):
#             print(len(s) - i)
#             break
#         cnt[1 - int(s[i])] -= 1