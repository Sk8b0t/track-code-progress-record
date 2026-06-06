# s= "abcddabac"
s="abcabcbb"
# s=list(a)
dict={}
l=r=0
ml=0
while(r<len(s)):
    if s[r] in dict :
        if dict[s[r]]>=l:
            l=dict[s[r]]+1
    dict[s[r]]=r
    ml=max(ml,r-l+1)
    r+=1
print(ml)