Hint 1
Try using two for loops to sum all possible pairs of numbers in the input array. What are the space and time implications of this approach?

Hint 2
Realize for every number X in the input array, you are essentially trying to find a corresponding number Y such that X + Y = targetSum. With this two variables in this section known to you, it shouldn't be hard to solve for Y.

Hint 3
Trying storing every number in hash table, solving the equation from Hint 2 for every number, and checking Y that you find is stored in the hash table. What are the time and space implications of this approach?