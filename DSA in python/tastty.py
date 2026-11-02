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
        if(t1==None):
            self.head=temp
        else:
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp

    def insertAtBeg(self,data):
        t1=self.head
        temp=node(data)
        self.head=temp
        temp.next=t1

    def insertInBetween(self,data,x):
        t1=self.head
        temp=node(data)
        while(t1!=None):
            if(t1.data==x):
                temp.next=t1.next
                t1.next=temp
            t1=t1.next

    def deleteLL(self,data):
        t1=self.head
        prev=t1
        if(t1.data==data):
            self.head=t1.next
        while(t1.next!=None):
            if(t1.data==data):
                prev.next=t1.next
                break
            prev=t1
            t1=t1.next
        if(t1.data==data):
            prev.next=None
            
    def printLL(self):
        t1=self.head
        while(t1.next!=None):
            print(t1.data)
            t1=t1.next
        print(t1.data)

obj=SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtBeg(69)
obj.printLL()
        
        