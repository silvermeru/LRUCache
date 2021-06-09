import Queue
import Node



# The LRUCache is a data cache with the eviction policy to remove the least recently used item
# size: the number of data blocks currently in the cache
# maxSize: the maximum number of data blocks allowed to be in the cache
# queue: a doubly linked list used to manage the next block of data marked for eviction
# data: a dictionary which stores Doublely linked list nodes
class LRUCache():
	def __init__(self, maxSize):
		self.size = 0
		self.maxSize = maxSize
		self.queue = Queue.Queue()
		self.nodes = {}

	# Put the value into the Cache and update the Queue accordingly.
	# If the cache is full then evict the least resently used data block as managed by the queue
	def put(self, key, value):

		# If the key is already in the cache we do not need to add a new datablock to the cache just update the one that is already there
		# We must ensure that the usage of the data is reflected in the Queue
		if key in self.nodes:
			node = self.nodes.get(key)
			node.value = value
			self.queue.useNode(node)

		else:
			# If we are adding a new data block we must make sure we are not exceding the maxSize
			# If we are exceding maxSize we must evict.
			if self.size == self.maxSize:
				# Since evict will return the linked list node
				self.nodes.pop(self.queue.evict())

			else:

				self.size += 1
			newNode = Node.Node(key, value)
			self.queue.addNode(newNode)
			self.nodes[key] = newNode

	# Get the value in associated with the given key
	# Update the Queue accordingly
	def get(self, key):
		node = self.nodes.get(key)
		if node != None and self.queue.useNode(node):
			print(node.data)


	# Remove the data associated with the given key and update the Queue accordingly
	def dele(self, key):
		delNode = self.nodes.get(key)

		if delNode != None:
			self.queue.removeNode(delNode)
			self.nodes.pop(key)
			self.size -=1


	# Empty the Cache and Queue
	def reset(self):
		self.queue.empty()
		self.nodes = {}
		self.size = 0