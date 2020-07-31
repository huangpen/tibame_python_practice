#!/usr/bin/env python3

def findClosestValueInBst(tree, target):
    # Write your code here.
    # Tip: Try define another helper function
    #      Try to write it using recursive and iterative method.








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
