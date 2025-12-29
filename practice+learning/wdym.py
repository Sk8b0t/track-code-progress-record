from functools import reduce
if __name__ == '__main__':
    # l = ["sayan", "nayas", "njr", "NeymarJr"]
    # a=' and '.join(l)
    # print(type(a))
    # print(a)

    # lst = [1, 2, 3, 43, 5, 66, 7, 69, 6]
    # print(list(map(lambda x: x * x, lst)))


    # map function returns object takes a function and applies it to each elements of a list
    # square= lambda x:x*x
    # cube=lambda x:x**3
    #
    # lst2 = [square, cube]
    # for i in range(5):
    #     print(list(map(lambda x: x(i), lst2)))


    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 69]
    def greaterthan5(n):
        return n > 6
    print(list(filter(greaterthan5, lst1)))
    print(reduce(lambda x,y:x+y, lst1))
