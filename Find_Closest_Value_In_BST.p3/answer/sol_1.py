#!/usr/bin/env python3


# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space

"""
On any node we calculate any absolute difference between target and node value, and compare to the next one. Stops when we reach minimum difference. If node value greater than target, traverse left. And vice versa.

recursive method:
Since everytime it calls findClosestValueInBstHelper from itself, it creates new stack stored in memory. If we have a balanced tree, the depth of the tree will be log(n) where n is the number of nodes, and we will traverse in at most log(n) steps. A like-balanced tree is will contribute to most cases, thus we have average O(log(n)) time. However, if we have entirely skewed tree which for example only left occuring nodes, we have to travese at most each nodes to find the target. Hence worst case O(n) time.
For space, during each of O(log(n)) steps in a balanced tree, we create a stack for each one, thus space complexity is (O(log(n))). Likewise, for worst case senario.
"""
def findClosestValueInBst(tree, target):
    # Write your code here.
    # Tip: Try define another helper function
    #      Try to write it using recursive and iterative method.
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest



# Testing
if __name__ == '__main__':
    import json
    import debug_v1
    import tree_class as tcls
    
    with open('test.json', 'r') as t:
        load_test = json.load(t)
        test_case = load_test['test']
        correct_output = load_test['answer']


    for count, case in enumerate(test_case):
        print(f'Test Case {count+1}:', end=' ')

        for each in case['tree']['nodes']:
            if case['tree']['root'] == each['id']:
                tree  = tcls.treeNode(each['id'], each['value'])
        tree.build_tree(case['tree']['nodes'])
                
        value = findClosestValueInBst(tree, case['target'])
        debug_v1.debug(case, value, correct_output[count])
