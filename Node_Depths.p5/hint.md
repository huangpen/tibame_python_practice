# Node Depths [Hint]

### This section provides one or more hints. Later hints gives more detail! Try to think before you check hints.

<details>
  <summary>
  Hint 1
  </summary>
  
As obvious as it may seem, to solve this question, you'll have to figure out how to compute the depth of any given node; once you know how to do that, you can compute all of the depths and add them up to obtain the desired output.
</details>



<details>
  <summary>
    Hint 2
  </summary>
  
To compute the depth of a given node, you need infomration about its position in the tree. Can you pass this information down from the node's parent?
</details>



<details>
  <summary>
  Hint 3
  </summary>

The depth of any node in the tree is equal to the depth of its parent node plus 1. By starting at the root node whose depth is 0, you can pass down to every node in the tree its respective depth, and you can implement the algorithm that does this and that sums up all of the depths either recursively or iteratively.
</details>
