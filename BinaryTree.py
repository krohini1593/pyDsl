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
        if self.left:
            print self.left.display()
        if self.right:
            print self.right.display()

         print self.data

    def lookup(self,data,parent=None):
    	if data < self.data:
    		if self.left is None:
    			return None, None
    		return self.left.lookup(data,self)
    	elif data > self.data :
    		if self.right is None:
    			return None, None
    		return self.right.lookup(data,self)
    	else:
    		return self, parent

root=Node(8)
root.display_inorder()

