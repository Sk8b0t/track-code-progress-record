
def solve(n,k):
    if(n==k==1):
        return 0;
    mid=2*(n-1)
    if(k<=mid):
        return solve(n-1,k)
    else:
         return 1-solve(n-1,k-mid)

    
if __name__ == "__main__":
    print(solve(2,2))