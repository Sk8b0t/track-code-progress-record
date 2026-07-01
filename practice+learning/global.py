# num=12
# def func(n):
#     global  num
#     num+=22
#     print(n , num )
#
# func("yo what the hell")

def sayan():
    x = 20

    def sia():
        global x
        x = 99

    print("before calling sia()", x)
    sia()
    print("after calling sia()", x)


sayan()
print(x)
