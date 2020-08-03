# Find Closest Value in BST [Hint]

### This section provides one or more hints. Later hints gives more detail! Try to think before you check hints.

<details>
  <summary>
  Hint 1
  </summary>
  
Try traversing the Binary Tree in a depth-first-search-like fashion.
</details>



<details>
  <summary>
    Hint 2
  </summary>
  
Recursively traverse the Binary Tree in a depth-first-search-like fashion, and pass a running sum of the values of every previously-visited node to each node that you're traversing.
</details>



<details>
  <summary>
  Hint 3
  </summary>

As you recursively traverse the tree, if you reach a leaf node(a node with no "left" or "right" Binary Tree nodes), add the relevant running sum that you've calculated to a list of sums(which you'll also have to pass to the recursive function). If you reach a node that isn't a leaf node, keep recursively traversing its children nodes, passing the correctly updated running sum to them.
</details>
