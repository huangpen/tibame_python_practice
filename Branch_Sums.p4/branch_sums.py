#!/usr/bin/env python3

def branchSums(root):
    # Write your code here.
    # Tip: Try define another helper function
    # This is the demonstration class of the input root. Do not edit it.
    # class BinaryTree:
    #   def __init__(self, value):
    #     self.value = value
    #     self.left = None
    #     self.right = None






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
        value = branchSums(tree)
        debug_v1.debug(case, value, correct_output[count])
