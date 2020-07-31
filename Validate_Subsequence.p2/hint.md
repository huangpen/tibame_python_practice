# Validate Subsequence [Hint]

### This section provides one or more hints. Later hints gives more detail! Try to think before you check hints.

<details>
  <summary>
  Hint 1
  </summary>

You can solve this question by iterating through the main input array once.
</details>



<details>
  <summary>
    Hint 2
  </summary>
  
Iterate through the main array, and look for the first integer in the potential subsequence. If you find that integer, keep on iterating through the main array, but now look for the second integer in the potential subsequence. Continue this process until you either find every integer in the potential subsequnce or you reach the end of the main array.
</details>



<details>
  <summary>
  Hint 3
  </summary>
  
To actually implement what Hint 2 describes, you'll have to declare a variable holding your position in the potential subsequence. At first, this position will be the 0th index in the sequenc; as you find the sequence's integers in the main array, you'll increment the position variable until you reach the end of the sequence.
</details>
