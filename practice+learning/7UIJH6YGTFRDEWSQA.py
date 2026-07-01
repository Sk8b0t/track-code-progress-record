def sum():
    """prints sum if the inputs are integer or throws error if not"""
    n1 = input("Enter a number:")
    n2 = input("Enter a number:")
    try:
        print("sum=", int(n1) + int(n2))
    except Exception as e:
        print("Error: ", e)

    print("Use of try catch is nutzz")


sum()
print("docstring : ", sum.__doc__)
