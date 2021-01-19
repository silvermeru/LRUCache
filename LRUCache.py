import Queue
import Node



# The LRUCache is a data cache with the eviction policy to remove the least recently used item
# size: the number of data blocks currently in the cache
# maxSize: the maximum number of data blocks allowed to be in the cache
# queue: a doubly linked list used to manage the next block of data marked for eviction
# data: a dictionary which stores datablocks by keys 
class LRUCache():
	def __init__(self, maxSize):
		self.size = 0
		self.maxSize = maxSize
		self.queue = Queue.Queue()
		self.data = {}

	# Put the value into the Cache and update the Queue accordingly.
	# If the cache is full then evict the least resently used data block as managed by the queue
	def put(self, key, value):

		# If the key is already in the cache we do not need to add a new datablock to the cache just update the one that is already there
		# We must ensure that the usage of the data is reflected in the Queue
		if key in self.data:
			self.data[key] = value
			self.queue.useNode(key)

		else:
			# If we are adding a new data block we must make sure we are not exceding the maxSize
			# If we are exceding maxSize we must evict.
			if self.size == self.maxSize:
				# Since evict will return the key to value 
				self.data.pop(self.queue.evict())

			else:

				self.size += 1

			self.queue.addNode(Node.Node(key))
			self.data[key] = value

	# Get the value in associated with the given key
	# Update the Queue accordingly
	def get(self, key):
		if self.queue.useNode(key):
			print(self.data[key])


	# Remove the data associated with the given key and update the Queue accordingly
	def dele(self, key):
		delNode = self.queue.getNode(key, self.queue.mru)

		if delNode != None:
			self.queue.removeNode(delNode)
			self.data.pop(key)
			self.size -=1


	# Empty the Cache and Queue
	def reset(self):
		self.queue.empty()
		self.data = {}
		self.size = 0