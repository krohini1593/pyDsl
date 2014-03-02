class Stack:
	
	stack=[]
	
	def __init__(self, data):
		self.data=data
		self.stack.append(data)

	def push(self,data):
		self.stack.append(data)

	def pop(self):
		return self.stack.pop()
		
	def display(self):
		print self.stack

	def peek(self):
		return self.stack[-1]