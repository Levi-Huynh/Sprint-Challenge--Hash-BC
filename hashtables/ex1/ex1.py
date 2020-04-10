#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    results = []
    # weights= [4,6,10,15,16] #21
    mydict = dict(list(enumerate(weights)))
    newdict = dict([(value, key) for key, value in mydict.items()])
    # new dict = {4:0, 6:1, 10:2, 15:3, 16:4 } {w:k}
    print(mydict)
    print(newdict)


    for k, v in newdict.items():
        hash_table_insert(ht, k, v)

    for wts in weights:
        myItem = limit - wts
        # same weight alwasy in same index 4 @ index 1 in this case always
        found = hash_table_retrieve(ht, myItem)
        #if found in results:
            #found = weights.index(myItem)
        if found is not None and found not in results:
            results.append(found)
    sortedL = sorted(results, reverse=True)
    newT = tuple(sortedL)
    print(newT, len(newT))
    if len(newT) <= 1:
        return None
    else:
        print(newT)
        return newT

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
