import LRUCache
import Queue
import Node

if __name__ == "__main__":

	q = Queue.Queue()

	q.addNode(Node.Node("1"))
	q.addNode(Node.Node("2"))
	q.addNode(Node.Node("3"))

	q.useNode("2")

	print(q.getNode("2", q.mru).key)

	print("mru: " + q.mru.key)
	print("lru: " + q.lru.key)
	print("evicted: " + q.evict())
	print("lru: " + q.lru.key)


	# Init Cache to size 5
	lruCache = LRUCache.LRUCache(5)
	# Fill Cache
	print("put1")
	lruCache.put("1","a")
	lruCache.get("1")
	print("put2")
	lruCache.put("2","b")
	print("put3")
	lruCache.put("3","c")
	print("put4")
	lruCache.put("4","d")
	print("put5")
	lruCache.put("5","e")

	# first element should still exist
	print("Get should return a")
	lruCache.get("1")

	# this should evict element 2
	print("put6 (evict 2)")
	lruCache.put("6","f")

	print("get2 should not find")
	lruCache.get("2")

	print("Delete 6")
	lruCache.dele("6")
	print("get 6")
	lruCache.get("6")
	print("reset")
	lruCache.reset()
	print("get 1")
	lruCache.get("1")






