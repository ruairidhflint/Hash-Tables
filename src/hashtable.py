# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        # Get index value of key
        index_value = self._hash_mod(key)
        # Check if index is currently empty
        if self.storage[index_value] is None:
            # Instantiate it to a Linked Pair (Class)
            self.storage[index_value] = LinkedPair(key, value)

        # If not, an item must already exist at that spot.
        else:
            # loop through the items at that index until we find the end (self.next is none)
            current_item = self.storage[index_value]

            while current_item.key != key:
                if current_item.next is None:
                    current_item.next = LinkedPair(key, value)
                    return
                else:
                    current_item = current_item.next
            
            current_item.value = value


    def print_stuff(self):
        for item in self.storage:
            print(item)

    def remove(self, key):
        # Hash the key to get the correct location
        index_value = self._hash_mod(key)
        # Set temporary variable to be the first item in the list
        current_value = self.storage[index_value]

        # if it's the first item in the list, set the first item to be the current items next value
        if current_value.key == key:
            self.storage[index_value] = current_value.next
        else:
            while current_value.next != key:
                if current_value.next is None:
                    return None
                else:
                    current_value = current_value.next
            
            current_value.next = current_value.next.next
        

    def retrieve(self, key):
        # Hash the key to get the correct location
        index_value = self._hash_mod(key)
        # set the current value variable to be the first item in the linked list at the correct index
        current_value = self.storage[index_value]
        # Loop through checking if the current key matches the key provided
        while current_value.next is not None:
            # if it matches, return the value
            if current_value.key == key:
                return current_value.value
            # otherwise move on to the next value
            else:
                current_value = current_value.next

                
        # once we reach the end of the chain, check the last value to see if it matches
        if current_value.key == key:
            return current_value.value
        else:
            return None



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
