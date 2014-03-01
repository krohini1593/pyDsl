class Node:

	def __init__(self,data):
		self.left=None;
		self.right=None;
		self.data=data;

	def display_inorder(self):
		if self.left:
			print self.left.display()
		print self.data
		if self.right:
			print self.right.display()

	def display_preorder(self):
                print self.data
                if self.left:
                        print self.left.display()
                if self.right:
                        print self.right.display()
	
	def display_postorder(self):
                print self.data
                if self.left:
                        print self.left.display()
                if self.right:
                        print self.right.display()

root=Node(8)
root.display_inorder()

