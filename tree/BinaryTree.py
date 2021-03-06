class BinarySearchTree:

	def __init__(self,data):
		self.left=None;
		self.right=None;
		self.data=data;

	def display_inorder(self):
		if self.left:
			print self.left.display_inorder()
		print self.data
		if self.right:
			print self.right.display_inorder()

	def display_preorder(self):
        	print self.data
        	if self.left:
                	print self.left.display_preorder()
        	if self.right:
                	print self.right.display_preorder()
	
	def display_postorder(self):
                if self.left:
           		 print self.left.display_postorder()
       		if self.right:
           		 print self.right.display_postorder()
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

root=BinarySearchTree(8)
root.display_inorder()

