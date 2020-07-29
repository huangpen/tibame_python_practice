# Two Number Sum [Hint]

### This section provides one or more hints. Later hints gives more detail! Try to think before you check hints.

<details>
  <summary>
  Hint 1
  </summary>
  
Try using two for loops to sum all possible pairs of numbers in the input array. What are the space and time implications of this approach?
</details>



<details>
  <summary>
    Hint 2
  </summary>
  
Realize for every number X in the input array, you are essentially trying to find a corresponding number Y such that X + Y = targetSum. With this two variables in this section known to you, it shouldn't be hard to solve for Y.
</details>



<details>
  <summary>
  Hint 3
  </summary>
  
Trying storing every number in hash table, solving the equation from Hint 2 for every number, and checking Y that you find is stored in the hash table. What are the time and space implications of this approach?
</details>
