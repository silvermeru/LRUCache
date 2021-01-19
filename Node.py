# A Node to be used in a doubly linked list.
# Keeps track of a Key to retreive data from cache.
# Key: Key to a piece of data stored in a dictionary.
# prev: previous node in the linked list.
# next: next node in the linked list
class Node:
	def __init__(self, key):
		self.key = key
		self.prev = None
		self.next = None