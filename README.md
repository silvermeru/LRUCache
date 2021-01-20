# LRUCache
A simple least recently used cache implemented in python using a doubly-linked list queue with a dictionary.

# To run
To run program from the command line run:
python -i LRUCache

The LRUCache constructor take an integer to define the number of data blocks to accept before evicting. eg: lru = LRUCache(10)

# Commands over the LRUCache:


put(key, value) - put takes a key and value and places it in the cache and queue. Takes O(1) time.

get(key) - get returns the value that has been stored with the given key value. This updates the queue accordingly. If the key is not currently stored, this returns nothing. Takes O(1) since size is defined at runtime and constant.

dele(key) - removes the associated data block from the cache and removes the key from the queue.Takes O(1) time. Note: del was not used because it is a protected keyword in python that should not be over written.

reset() - clears the cache and Queue. Takes O(1) time since size is constant


# Contents
Main.py - used for local testing. A full battery of testing to come.

Node.py - Contains the Node class used by the Queue class.

Queue.py - My implementation of a Doubly linked list. A doubly linked list was chosen for managing the the Queue becuase it allows for constant time put and get commands. A bitwise implementation could have also been used.

LRUCache.py - My implementation of the LRU cache

# Goal
It was my goal with this project to not import any modules provided outside of base python. Everything I needed I designed from scratch. In the future I would extend unit testing with a unitesting framework to ensure better coverage. I used a doubly-linked list as a queue for the high reduction in timing it offers in putting and evicting data blocks into the dictionary.

# Future Goal
Implement other queuing systems such as using a counter with an addicitonal dictionary or a single linked list. I would like to compare different timings of these different queuing systems to identify which queuing systems optimize which operations the most.
