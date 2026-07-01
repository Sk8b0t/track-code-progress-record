#lst = [3,3,3,3,3,999,99,999]
n1=input("Enter a word :")
n2=input("Enter a word :")
s=set()
s1=set()
for l in n1:
    s.add(l)
for l in n2:
    s1.add(l)
if s==s1:
    print("anagram")
#diff btw discard() and remove()
# remove() generates error if the element is not in set but discard() doesn't generate error


