wrd = ""
sen = input("Enter a sentence:")
sen += " "
for i in range(len(sen)):
    if sen[i] != " ":
        wrd += sen[i]
    else:
        print(wrd[::-1], end=" ")
        wrd = ""
