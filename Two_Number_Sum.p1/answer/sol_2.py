#!/usr/bin/env python3

def twoNumberSum(array, targetSum):
    # Write your code here.

    # O(n) time | O(n) space
    '''
      dictionary(or hashtable) creates fast key value access, so the time
      complexity contributor comes from the for loop alone. Since the creation
      of dictionary and storing varibles will vary according to input sizes,
      it renders linear complexity.
    '''
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []








# Testing
if __name__ == '__main__':
    import json
    import debug_v1

    with open('test.json', 'r') as t:
        load_test = json.load(t)
        test_case = load_test['test']
        correct_output = load_test['answer']

    for count, case in enumerate(test_case):
        print(f'Test Case {count+1}:', end=' ')
        value = twoNumberSum(case['array'], case['targetSum'])
        debug_v1.debug(case, value, correct_output[count])
