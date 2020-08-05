## Node Depths

The distance between a node in a Binary Tree and the tree's root is called the node's depth.

Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.

Each **BinaryTree** node has an integer **value**, a **left** child node, and a **right** child node. Children nodes can either be **BinaryTree** nodes themselves or **None** / **null**.


### Sample Input:
	
	tree =       1
	     	  /    \
		 2      3
		/ \    / \
	       4   5  6   7
	      / \     
         8  9    
	

### Sample Output:
	
	16
	// The depth of the node with value 2 is 1.
	// The depth of the node with value 3 is 1.
	// The depth of the node with value 4 is 2.
	// The depth of the node with value 5 is 2.
	// Etc...
	// Summing all of these depths yields 16.


### Note:

   A Binary Tree is represented by a list of **nodes** and a **root** node. Every node has to have a unique string **id** that will be referenced by other nodes' **left** and **right** pointers and by the root. A data structure example of the above is shown below:

       {
         "nodes": [
    	    {"id": "1", "left": "2", "right": "3", "value": 1},
    	    {"id": "2", "left": "4", "right": "5", "value": 2},
    	    {"id": "3", "left": "6", "right": "7", "value": 3},
    	    {"id": "4", "left": "8", "right": "9", "value": 4},
    	    {"id": "5", "left": null, "right": null, "value": 5},
    	    {"id": "6", "left": null, "right": null, "value": 6},
    	    {"id": "7", "left": null, "right": null, "value": 7},
    	    {"id": "8", "left": null, "right": null, "value": 8},
    	    {"id": "9", "left": null, "right": null, "value": 9}
  	     ],
  	     "root": "1"
       }
       
The code representation of Binary Tree is of class construct, something like this:

	class BST:
    	def __init__(self, value):
        		self.value = value
        		self.left = None
        		self.right = None
