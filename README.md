# LRUCache
A simple least recently used cache implemented in python using a doubly-linked list queue with a dictionary.


To run program from the command line run:
python -i LRUCache

The LRUCache constructor take an integer to define the number of data blocks to accept before evicting.

Commands over the LRUCache:
put(key, value) - put takes a key and value and places it in the cache and queue. Takes O(1) time
get(key) - get returns the value that has been stored with the given key value. This updates the queue accordingly. Takes O(1) since size is defined at runtime and constant
dele(key) - removes the associated data block from the cache and removes the key from the queue.Takes O(1) time. Note: del was not used because it is a protected keyword in python that should not be over written.
reset() - clears the cache and Queue. Takes O(1) time since size is constant

