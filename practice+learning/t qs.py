def printShit(lst):
  for i in lst:
      print(i)

def sameShit(*tmkc, **kwargs):
    """*-> list(optional; not compulsory) in a function argument  *args
      **-> dictionary(optional; not compulsory) in a function argument  **kwargs"""
    for i in tmkc:
        print(i)

    for key in kwargs:
        print(key , kwargs[key])

l=["sayan", "nayas", "njr","NeymarJr"]
d={"sayan":1, "nayas":2, "njr":3,"NeymarJr":4}
#printShit(l)
sameShit(*l,**d)
print(sameShit.__doc__)
