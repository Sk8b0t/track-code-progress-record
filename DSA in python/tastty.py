class node:
    def __init__(self,data,nxt=None,prev=None):
        self.data=data
        self.next=nxt
        self.prev=prev

class CircularLinkedList:
    def __init__(self,head=None):
        self.head=head

    def insertAtEnd(self,data):
        t=self.head 
        temp=node(data)
        while(t.next!=self.head):
            t=t.next
        temp.next=self.head
        temp.prev=t
        t.next=temp

    def insertInBetween(self,data,x):
        t=self.head
        temp=node(data)
        while(t.next!=self.head):
            if(t.data==x):
                break
            t=t.next
        if(t.data==x):
            temp.next=t.next
            temp.prev=t
            t.next=temp

