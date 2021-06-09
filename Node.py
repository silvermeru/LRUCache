# A Node to be used in a doubly linked list.
# Keeps track of a data that will be retrieved from the cache.
# data: data that is stored associated with a key
# key: key to the 
# more: the node more recently used than this one
# less: the node les recently used than this one
class Node:
	def __init__(self, key, data):
		self.key  = key
		self.data = data
		self.more = None
		self.less = None