# Stack Implementation using Array




class Stack():
  def __init__(self,value):
    self.myStack = []
    self.myStack.append(value)
    self.printList()
  
  def push(self, value):
    self.myStack.append(value)
    self.printList()
    
  
  def pop(self):
    if len(self.myStack) > 0:
      self.myStack.pop()
    self.printList()
    

  def printList(self):
    print("Stack: ", self.myStack)
    

  def peak(self):
    print("Peak is: " , self.myStack[len(self.myStack)-1])




myStack = Stack('100')
myStack.push('200')
myStack.peak()
myStack.push('300')
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()




