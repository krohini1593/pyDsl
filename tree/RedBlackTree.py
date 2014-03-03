class RedBlackTree:
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data
		self.color="BLACK"
		self.root=self
		
		
	def insert_location(self,data): #insert node at its proper place
	        newNode=RedBlackTree(data)
		newNode.color="RED"
	
		if self.root is None:
			self.root=newNode
		else:
			node=self.root
		while True:
			if data <=node.data:
				if node.left is None:
					node.left=newNode
					newNode.parent=node
					break
				node=node.left
			else:
				if node.right is None:
					node.right=newNode
					newNode.parent=node
					break
				node=node.right
		return newNode	
	
	
	def insert(self,data): #First insert at location then adjust node to balance
		newNode=self.insert_location(data)
		#node Inserted Now Balance
		return newNode
	
		
	def display_inorder(self):
		if self.left:
			print self.left.display_inorder()
		print self.data,self.color
		if self.right:
			print self.right.display_inorder()

	def display_preorder(self):
        	print self.data,self.color
        	if self.left:
                	print self.left.display_preorder()
        	if self.right:
                	print self.right.display_preorder()
	
	def display_postorder(self):
                if self.left:
           		 print self.left.display_postorder()
       		if self.right:
           		 print self.right.display_postorder()
	       	print self.data,self.color
rb=RedBlackTree(5)
rb.insert(6)
rb.insert(4)
rb.insert(2)
rb.insert(10)
rb.display_preorder()


