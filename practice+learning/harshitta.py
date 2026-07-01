with open("Mary Kom.txt", "r+") as f:
    for item in f.readlines():
        for p in [",", "?", ":", "."]:
            item = item.replace(p, "")
        wrdlst = item.lower().split()
        for i in wrdlst:
            if i == i[::-1]:
                print(i)
