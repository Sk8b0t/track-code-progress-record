class tf:
    no_of_likes=2
    def __init__(self,n,l1,l2):
        self.name=n
        self.like1=l1
        self.like2=l2

    def printLike(self):
        return f"{self.name} 1stly likes {self.like1} and then {self.like2}"
    @classmethod
    def changeLikes(cls,likes):
        cls.no_of_likes=likes


nayas=tf("Nayas","pookie","Narla")
sayan=tf("Sayan","Pookie","Sia")
# sayan.like1="pookie"
# sayan.name="Sayan"
nayas.name="Nayas"
# sayan.like2="sia"
nayas.like=["sia", "pookie"]

print(sayan.like2,nayas.like)
print(sayan.no_of_likes)
print(tf.no_of_likes)
print(nayas.no_of_likes)
sayan.no_of_likes=3
print(sayan.__dict__)
print(nayas.__dict__)
print(sayan.printLike())
sayan.changeLikes(4)
