import LRUCache
import Queue
import Node

if __name__ == "__main__":

	print("TESTING QUEUE")
	q = Queue.Queue()

	print("adding nodes 1,2,3")
	nodeA = Node.Node("1", "a")
	nodeB = Node.Node("2", "b")
	nodeC = Node.Node("3", "c")

	q.addNode(nodeA)
	q.addNode(nodeB)
	q.addNode(nodeC)

	print("Using 2")
	q.removeNode(nodeB)
	q.addNode(nodeB)

	print("mru expect 2: " + q.mru.key)
	print("lru expect 1: " + q.lru.key)
	print("evicted expect 1: " + q.evict())
	print("lru expect 3: " + q.lru.key)

	print("TESTING LRUCACHE")
	# Init Cache to size 5
	lruCache = LRUCache.LRUCache(5)
	# Fill Cache
	print("put 1 as a")
	lruCache.put("1","a")
	print("get 1. Expect a")
	lruCache.get("1")
	print("put 1 as f")
	lruCache.put("1","f")
	print("get 1. Expect f")
	lruCache.get("1")
	print("put 2")
	lruCache.put("2","b")
	print("put 3")
	lruCache.put("3","c")
	print("put 4")
	lruCache.put("4","d")
	print("put 5")
	lruCache.put("5","e")

	# first element should still exist
	print("Get 1 should return f")

	# this should evict element 2
	lruCache.get("1")

	print("put 6 should evict 2")
	lruCache.put("6","f")

	print("get 2 should not find because it was evicted")
	lruCache.get("2")

	print("Delete 6")
	lruCache.dele("6")
	print("get 6 should not find because it was evicted")
	lruCache.get("6")
	print("reset")
	lruCache.reset()
	print("get 1 should not find because everything is empty")
	lruCache.get("1")