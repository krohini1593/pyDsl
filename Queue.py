class Queue:
	queue=[]

	def __init__(self,data):
		self.data=data
		self.queue.append(data)

	def insert_front(self,data):
		self.queue.insert(0,data)

	def insert_rear(self,data):
		self.queue.append(data)

	def delete_front(self):
		return self.queue.pop(0)

	def delete_rear(self):
		return self.queue.pop()

	def display(self):
		print self.queue

	def peek_front(self):
		return self.queue[0]

	def peek_rear(self):
		return self.queue[-1]