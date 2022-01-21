# Stack Implementation using Linked List
class Node():
  def __init__(self,value):
    self.data = value
    self.next = None




class Stack():
  def __init__(self,value):
    newNode = Node(value)
    self.head = newNode
    self.tail = newNode
    self.length = 1
    self.printList()
  
  def push(self, value):
    newNode = Node(value)
    prevHead = self.head
    self.head = newNode
    self.head.next = prevHead
    self.length += 1
    self.printList()
    
  
  def pop(self):
    if self.length > 0:
      self.head = self.head.next
      self.length -= 1
    self.printList()
    

  def printList(self):
    currentNode = self.head
    stack = []
    while currentNode is not None:
      stack.append(currentNode.data)
      currentNode = currentNode.next
    print("Stack is: ", stack, " With length: ", self.length)
    

  def peak(self):
    print("Peak Is: ",self.head.data)




myStack = Stack('100')
myStack.push('200')
myStack.peak()
myStack.push('300')
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()




