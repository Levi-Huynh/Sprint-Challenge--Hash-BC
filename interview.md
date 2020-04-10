# Arrays

Objectives:
1) understand memory structure of an array
2) understand how inserting into an array works
3) Know the diff between arrays & Python lists  

1) array:
    Seq of elements of the same type, stored in a contiguous block of memory

How to declare array?
1) determine how big the array needs to be 
2) request a block of memory that will fit the array 
3) recieve the memory address of the reserved block
4) write your values into memory

Declare the array: [2,3,4,5]

1. determine how big the array needs to be
    - `an integer is 4-bytes so the array needs to be 16-bytes`
    - `byte consists of 4 bits, bit is either 1 or 0`
2. Request a block of memory that will fit the array    
    - `rquest 16-bytes of memory from the computer`
3. Recieve the memory address of the reserved block 
    -`recieve an address to the start of the 16-bytes of reserved memory`
4. Write your values into the array 

Advantages:
-Space and time efficient
//each element must be the same type 
//sequential
//continuous block of memory

# Add to Array 
1. take size of current array & increase it by one element 
2. Req a block of memory of the new size (if 4 bytes/int, array of 5 int=20bytes, array 4 int=16 bytes)
3. Copy each element from old space to the new space one byte at a time // this is the SLOW PART! 
    -kind of like the swap space 
4. free the memory from the old array 
    -This is an O(n) operation 
    -the old specific sized 16 block of memory for array of 4 int, is now not being used. Leads to 
    `fragmentation` . Little tiny memory slots that can only store specifically 4 integers.

# HOW DOES PYTHON ADD AN ELEMENT TO THE begining OF A LIST?
1. Check if theres any empty space at the end of the array 
2.  If not: 
    1) allocate a new array, pace the first lement and copy over the test
    2) Free memory from the old array 
3 If so: 
    1) starting at back, move Each element to the right one space 
    2) Place new element in first position 
    O(n) operation no matter what for insert into front!!! 

    Explain in detail the workings of a dynamic array:
What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
`ARRAY RTC`:
-`ACCESS`- O(1)
-`REMOVE/ADD (FRONT)`- O(n) must shfit everything to right 
-`REMOVE/ADD (BACK)`- O(1) No need to shift elements
-`SEARCH` - O(n)

`HT RTC`:
-`ACCESS`-  O(1) BEST, WORSE O(n)
-`REMOVE/ADD (FRONT)`-best case O(1), worse O(n)
-`REMOVE/ADD (BACK)`- best case O(1) worse O(n)
-`SEARCH` - O(1)  bset case, worse O(n)
^O(n) occurs if ds holding other k,v pairs in 
bucket needs to be traversed 


`What is the worse case scenario if you try to extend the storage size of a dynamic array?`
O(n) must traverse through buckets that have 
LL or other DS that needs traversing also recopy each element over 1 by 1

# BLOCKCHAIN, CHAIN
`Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?`

# BLOCKCHAIN STRUCTURE:
-data structre & support system to keep a public ledger of transactions
-anyone can make a copy
-everyone has access to the source code 
-yet it is still secure, thanks to the clever use of cryptography

# BLOCK has 
-Index Number
-Timestamp 
-List of Transactions
-Proof used to Mine this Block #very complicated computation 
-Crptographic Hash of Previous Block (links all of the blocks together)

  -^^ Crypto HF on all the data of a prev block, we get a unique representation fo that block thats difficult to fake & modify,
  modification of any blocks already mined will not fit the `crypto hashed prev entry of for blocks you modify will not fit with the entry already writen for it on the next block ` You would have to correctly match all of the `prev block hashes` & get it to pass for the rest of the blocks in the chain increasing your computation work, and do it before some mines a new block 
  -HF must be deterministic (same input must result in same output, no percieved pattern between input/output good distribution)



Chain:
-Blocks are chained together using a crypto hash of the prev
block entry (via proof of work)
# Data is organized:
- Created by stringing together hashes
- Start with Genesis Block 
    -manually created
    -from that point forwards, each block forward contains the hash of the previous block 
    -prev block has a hash of the one before that 

-`proof of works protects chain against hackers by`:
    -if bad actor changes the transactions in any of the blocks, the nextblock's prev. hash attribute will not match 
    the hash from previous block. Identitying blocks that are compromised 
    - can't redo, all of the hashes through rest of chain due to "proof" of work


# PROOF OF WORK
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?
-proof of work is an arbitrarily(6-70 leading zeros) difficult problem, that takes a large amount of computation to return/solve/satisfy
-by `requiring a solution that uses the hash of the previous block, plus a new value, work can't start ahead of time (must have the prev block forged correctly) & can't be reused`
-`The difficult can be tuned to allow a consistent discovery of proofs, regardless of the total effort spent`
-This protects the blockchains by making it very difficult to generate a new block  
 # `#guess is 
        #just an encoding of the prev block's hash & some algo/random number
        #that must pass specified difficulty such as having certain number of leading zeros`