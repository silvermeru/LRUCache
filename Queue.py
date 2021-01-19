import Node

# queue tracks the order of data to remove from the cache.
# length: The current length of the queue
# maxSize: The maximum size the queue can reach
# lru: The least recently used piece of data.
# mru: The node corresponding to the most recently used piece of data.
# mru and lru are the extreme members of a doubly linked list.
# When a piece of data its corresponding node will be moved to mru spot. 
# This leaves the lru at the opposite end of the list to track the least recently used piece of data
class Queue:
	def __init__(self):
		self.lru = None
		self.mru = None

	# Remove the lru item from the queue and track the new lru item
	def evict(self):
		key = self.lru.key
		self.removeNode(self.lru)
		return key


	#Add a node to the queue.
	def addNode(self, node):
		# if mru is empty then there are currently no nodes in the queue so we can add without worrying about linking
		if self.mru == None:
			self.mru = node
			self.lru = node

		else:
			self.mru.next = node
			node.prev = self.mru
			self.mru = node


	# Remove a given node from the queue
	def removeNode(self, node):

		if node.next != None:
			node.next.prev = node.prev

		# If the node we are removing is the mru then we must update the mru.
		if self.mru.key == node.key:
			self.mru = node.prev

		if node.prev != None:
			node.prev.next = node.next

		# If the node we are removing is the lru then we must update the lru.	
		if self.lru.key == node.key:
			self.lru = node.next

		# Ensure references are cleared to prevent memory leaking
		node.prev = None
		node.next = None


		# Recursively find and get node of linked list by key.
	def getNode(self, key, node):
		if node == None:
			return None
		if node.key == key :
			return node
		else:
			return self.getNode(key, node.prev)


	# Move the node that contains this key to the mru slot in the in the queue
	# return false if the node corresponding to the key is not found
	def useNode(self, key):

		if self.mru == None:
			return False

		if self.mru.key == key:
			return True

		usedNode = self.getNode(key, self.mru.prev)

		if usedNode == None :
			return False

		self.removeNode(usedNode)
		self.addNode(usedNode)

		return True


	# empty all nodes from the queue
	def empty(self):
		while self.mru != None:
			self.removeNode(self.mru)

		self.mru = None
		self.lru = None
