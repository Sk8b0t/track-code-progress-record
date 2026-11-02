class node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class doublyLinkedList:
    def __init__(self,head=None):
        self.head=head

    def insertAtEnd(self,data):
        t=self.head
        temp=node(data)
        if(t==None):
            self.head=temp
            return
        while(t.next!=None):
            t=t.next
        t.next=temp
        temp.prev=t

    def insertAtBeg(self,data):
        t=self.head
        temp=node(data)
        if(t==None):
            self.head=temp
            return
        temp.next=t.next
        t.prev=temp
        self.head=temp

    def insertInBetween(self,data,x):
        t=self.head
        temp=node(data)
        while(t.next!=None):
            if(t.data==x):
                break
            t=t.next
        if(t.data==x):
            temp.next=t.next
            temp.prev=t
            t.next=temp

    def deleteDLL(self,data):
        t=self.head
        if(t.data==data):
            t=t.next
            t.prev=None
            return
        while(t.next!=None):
            if(t.data==data):
                t.prev.next=t.next
                t.next.prev=t.prev
                return
            t=t.next
        if(t.data==data):
            t.prev.next=None

    def printDLL(self):
        t=self.head
        while(t.next!=None):
            print(t.data)
            t=t.next
        print(t.data)

dll=doublyLinkedList()
dll.insertAtEnd(10)
dll.insertAtEnd(20)
dll.insertAtEnd(30)
dll.insertAtBeg(5)
dll.insertInBetween(699,20)
dll.deleteDLL(699)
dll.printDLL()
        

    
