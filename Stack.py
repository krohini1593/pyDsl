class Stack:
	
	stack=[]
	def __init__(self, data):
		self.data=data
		self.stack.append(data)

	def push(self,data):
		stack.append(data)

	def pop(self,data):
		return stack.pop()
		
	def display(self):
		print self.stack

stack=Stack(8)
stack.display()
