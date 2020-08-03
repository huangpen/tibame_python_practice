## Find Closest Value in BST

Write a function that takes in a Binary Search Tree (BST) and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.

A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts a root node and ends at any leaf node.

Each **BinaryTree** node has an integer **value**, a **left** child node, and a **right** child node. Children nodes can either be **BinaryTree** nodes themselves or **None** / **null**.


### Sample Input:
	
	tree =       1
	     	  /    \
		 2      3
		/ \    / \
	       4   5  6   7
	      / \  /   
             8   9 10    
	

### Sample Output:
	
	[15, 16, 18, 10, 11]
	// 15 == 1 + 2 + 4 + 8
	// 16 == 1 + 2 + 4 + 9
	// 18 == 1 + 2 + 5 + 10
	// 10 == 1 + 3 + 6
	// 11 == 1 + 3 + 7


### Note:

   A Binary Tree is represented by a list of **nodes** and a **root** node. Every node has to have a unique string **id** that will be referenced by other nodes' **left** and **right** pointers and by the root. A data structure example of the above is shown below:

       {
         "nodes": [
    	    {"id": "1", "left": "2", "right": "3", "value": 1},
    	    {"id": "2", "left": "4", "right": "5", "value": 2},
    	    {"id": "3", "left": "6", "right": "7", "value": 3},
    	    {"id": "4", "left": "8", "right": "9", "value": 4},
    	    {"id": "5", "left": "10", "right": null, "value": 5},
    	    {"id": "6", "left": null, "right": null, "value": 6},
    	    {"id": "7", "left": null, "right": null, "value": 7},
    	    {"id": "8", "left": null, "right": null, "value": 8},
    	    {"id": "9", "left": null, "right": null, "value": 9}
    	    {"id": "10", "left": null, "right": null, "value": 10}
  	     ],
  	     "root": "1"
       }
       
The code representation of BST is of class construct, something like this:

	class BST:
    	def __init__(self, value):
        		self.value = value
        		self.left = None
        		self.right = None
