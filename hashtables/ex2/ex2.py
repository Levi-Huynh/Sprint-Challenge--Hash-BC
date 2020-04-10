#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    ht = HashTable(length)
    route = [None] * (length-1)


    for elem in tickets:
        hash_table_insert(ht, elem.source, elem.destination)
    
    current_location = "NONE"

    for i in range((length-1)):
        route[i] = hash_table_retrieve(ht, current_location)

        print("route[i]", route[i])

        current_location = route[i]
        print("building route dynamic array", route)

    print("route final", route)
    return route 