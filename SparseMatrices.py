class SparseMatrix(object):
	
	matrix=[]

	def __init__(self, *data):
		for i in range(0,len(data)):
			self.matrix.append(data[i])

	def display(self):
		print self.matrix
