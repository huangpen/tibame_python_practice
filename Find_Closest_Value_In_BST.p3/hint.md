# Two Number Sum [Hint]

### This section provides one or more hints. Later hints gives more detail! Try to think before you check hints.

<details>
  <summary>
  Hint 1
  </summary>
  
Try traversing the BST node by node, all the while keeping track of the node with the value closest to the target value. Calculating the absolute value of the difference between a node's value and the target value should allow you to check if that node is closer than the current closest one.
</details>



<details>
  <summary>
    Hint 2
  </summary>
  
Make use of the BST property to determine what side of any given node has values close to the target value and is therefore worth exploring.
</details>



<details>
  <summary>
  Hint 3
  </summary>

What are the advantages and disadvantages of solving this problem iteratively as opposed to recursively?
</details>
