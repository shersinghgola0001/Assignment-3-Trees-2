Find sum of all nodes of the given perfect binary tree

def SumNodes(l):
	
	# no of leaf nodes
	leafNodeCount = pow(2, l - 1)

	# list of vector to store nodes of
	# all of the levels
	vec = [[] for i in range(l)]

	# store the nodes of last level
	# i.e., the leaf nodes
	for i in range(1, leafNodeCount + 1):
		vec[l - 1].append(i)

	# store nodes of rest of the level
	# by moving in bottom-up manner
	for i in range(l - 2, -1, -1):
		k = 0

		# loop to calculate values of parent nodes
		# from the children nodes of lower level
		while (k < len(vec[i + 1]) - 1):

			# store the value of parent node as
			# Sum of children nodes
			vec[i].append(vec[i + 1][k] +
						vec[i + 1][k + 1])
			k += 2

	Sum = 0

	# traverse the list of vector
	# and calculate the Sum
	for i in range(l):
		for j in range(len(vec[i])):
			Sum += vec[i][j]

	return Sum

# Driver Code
if __name__ == '__main__':
	l = 3

	print(SumNodes(l))
