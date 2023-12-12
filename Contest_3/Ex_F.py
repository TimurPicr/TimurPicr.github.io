tree = []
array = [1, 2, 3, 4, 5, 6, 7, 8]

		
def sort_tree(tree, index): #index_0 = len(tree) - 1
	if (index != 0):
		if (index % 2 == 0): #Правый
			if (tree[index] > tree[int(index/2-1)]):
				swap = tree[index]
				tree[index] = tree[int(index/2-1)]
				tree[int(index/2-1)] = swap
				sort_tree(tree, int(index/2-1))

		else: #Левый
			if (tree[index] > tree[int((index-1)/2)]):
				swap = tree[index]
				tree[index] = tree[int((index-1)/2)]
				tree[int((index-1)/2)] = swap
				sort_tree(tree, int((index-1)/2))	
	
aboba = list(map(int, input().split()))
for j in range(len(aboba)):
	for i in range(len(aboba) - 1, -1, -1):
		sort_tree(aboba, i)
	
for i in aboba:
	print(i, end=" ")
print('')
	
	
	
	
	
	
		
		
