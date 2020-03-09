'''

HASH TABLE IMPLEMENTATION (1st draft)


INSERT:
- Hash the key value. This will produce an integer of a large size.
- Perform a modulo operation on this new integer dividing by the capcity of the hashtable which will
provide a number between 0 and the length of the hashtable - 1.
- This new integer becomes the index at which we store the value.
- Two options are possible: 
    1.) The index is currently empty and therefore we can insert it without problem
    2.) The index is currently occupied. If this is the case, we should instantiate a linked list with our items that have the same index


'''

from hashtable import HashTable


ht=HashTable(3)

ht.insert('hello', 'world')
ht.insert('goodbye', 'sweet prince')

ht.print_stuff()
