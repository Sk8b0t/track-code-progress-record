x=int(input())
for i in range(1,10):
    y=x-((10**i)-1)
    if y>0 and len(str(y))==i:
        print(y)
        break
