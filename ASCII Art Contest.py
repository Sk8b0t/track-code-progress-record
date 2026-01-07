# Read three integers from input
g, c, l = map(int, input().split())

# Check if max - min >= 10
if max(g, c, l) - min(g, c, l) >= 10:
    print("check again")
else:
    # Otherwise print "final " + median
    print("final", sorted([g, c, l])[1])
