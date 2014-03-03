class Node:
	
	def __init__(self,data):
		self.data=data
		self.next=None


class LinkedList:

	def __init__(self):
		self.head=None
		self.tail=None

	def add_node(self,data):
		new_node=Node(data)

		if self.head==None:
			self.head=new_node

		if self.tail!=None:
			self.tail.next=new_node

		self.tail=new_node

	def delete_node(self,data):
		prev=None
		node=self.head
		
		while(node!=None) and (node.data!=data):
			prev=node
			node=node.next

		if prev==None:
			self.head=node.next
		else:
			prev.next=node.next

	def print_list(self):
		node=self.head

		while node!=None:
			print node.data
			node=node.next

	def search(self,data):
		prev=None
		node=self.head

		while (node!=None):
			prev=node
			if node.data == data:
				return True
			else:
				node=node.next
