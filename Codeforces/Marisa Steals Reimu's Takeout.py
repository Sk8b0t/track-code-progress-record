t = int(input())
while t:
    n = int(input())
    w = list(map(int, input().split()))
    zero = w.count(0)
    one = w.count(1)
    two = w.count(2)
    ans = zero
    p = min(one,two)
    ans += p
    one -= p
    two -= p
    ans += one // 3
    ans += two // 3
    print(ans)

    t -= 1