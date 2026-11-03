#peek ,pop,push,isEmpty->common fncs used in stack

class stack:
    def __init__(self):
        self.s=[]
    def push(self,value):
        self.s.append(value)
    def pop(self):
        if(len(self.s)==0):
            raise Exception("Stack is empty")
            return
        self.s.pop()
    def peek(self):
        if(len(self.s)!=0):
            return self.s[len(self.s)-1]
        else:
            raise Exception("Stack is Empty")

stk=stack()
stk.push(10)
stk.push(20)
stk.push(69)
stk.push(30)
stk.pop()
print(stk.peek())
        
        
        
    