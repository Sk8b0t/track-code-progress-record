a=[1,1,3,1]
fa={}
ele=a[0]
cnt=0
a.append(-1)
for i in range(len(a)):
        if a[i]==ele:
            cnt+=1
        else:
            if a[i-1] not in fa:
                fa[a[i-1]]=0
            fa[a[i-1]]=max(fa[a[i-1]],cnt)
            ele=a[i]
            cnt=1
print(fa)