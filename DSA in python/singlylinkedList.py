class node:
    def __init__(self,data,nxt=None):
        self.data=data
        self.next=nxt

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head

    def insertAtEnd(self,data):
        t1=self.head
        temp=node(data)
        if(t1!=None):
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp

    def insertAtBeg(self,data):
        temp=node(data)
        temp.next=self.head
        self.head=temp

    def insertInBetween(self,data,x):
        t1=self.head
        temp=node(data)
        while(t1.next!=None):
            if(t1.data==x):
                temp.next=t1.next
                t1.next=temp
            t1=t1.next
    def deleteLL(self,value):
        t1=self.head
        prev=t1
        if(t1.data==value):
            self.head=t1.next
        while(t1.next!=None):
            if(t1.data==value):
                prev.next=t1.next
                break
            prev=t1
            t1=t1.next
        if(t1.data==value):
            prev.next=None

    def printLL(self):
        t1=self.head
        while(t1.next!=None):
            print(t1.data)
            t1=t1.next
        print(t1.data)

obj1=SinglyLinkedList()
obj1.insertAtEnd(10)
obj1.insertAtEnd(20)
obj1.insertAtEnd(30)
obj1.insertAtEnd(69)
# obj1.insertAtBeg(112)
# obj1.insertInBetween(400,30)
# obj1.deleteLL(112)
obj1.printLL()






        