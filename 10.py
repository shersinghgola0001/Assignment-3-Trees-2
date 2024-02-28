Find maximum level sum in Binary Tree

from collections import deque

# A binary tree node has data, pointer
# to left child and a pointer to right
# child
class Node:
	
	def __init__(self, key):
		
		self.data = key
		self.left = None
		self.right = None

# Function to find the maximum sum
# of a level in tree
# using level order traversal
def maxLevelSum(root):
	
	# Base case
	if (root == None):
		return 0

	# Initialize result
	result = root.data
	
	# Do Level order traversal keeping
	# track of number
	# of nodes at every level.
	q = deque()
	q.append(root)
	
	while (len(q) > 0):
		
		# Get the size of queue when the
		# level order traversal for one
		# level finishes
		count = len(q)

		# Iterate for all the nodes in
		# the queue currently
		sum = 0
		while (count > 0):
			
			# Dequeue an node from queue
			temp = q.popleft()

			# Add this node's value to current sum.
			sum = sum + temp.data

			# Enqueue left and right children of
			# dequeued node
			if (temp.left != None):
				q.append(temp.left)
			if (temp.right != None):
				q.append(temp.right)
				
			count -= 1	

		# Update the maximum node count value
		result = max(sum, result)

	return result
	
# Driver code
if __name__ == '__main__':
	
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.right = Node(8)
	root.right.right.left = Node(6)
	root.right.right.right = Node(7)

	# Constructed Binary tree is:
	#			 1
	#		 / \
	#		 2	 3
	#	 / \	 \
	#	 4 5	 8
	#				 / \
	#			 6	 7	
	print("Maximum level sum is", maxLevelSum(root))
     
