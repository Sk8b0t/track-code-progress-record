#1
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
#2 - using set
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     kcnt=0
#     s=set()
#     for item in a:
#         if item==k:
#             kcnt+=1
#         if item<k:
#             if item not in s:
#                 set.add(item)                
#     print(max(k-len(s),kcnt))

#3 - using dictionary
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     cnt,kcnt=0=0
#     freq{}
#     for item in a:
#         if item not in freq:
#             freq[item]=1
#         else:
#             freq[item]+=1
#     i=0
#     while(i<k):
#         if i not in freq:
#             cnt+=1
#         i+=1
#     if k in freq:
#         kcnt=freq[k]

#     print(max(kcnt,cnt))
            
            
        


