import pickle
file="mypickle.pkl"
lst=["sayan","biswas","pookie","ferrari"]
with open(file,'wb') as f:
    pickle.dump(lst,f)

with open(file,'rb') as f:
    obj=pickle.load(f)
print(*obj)
