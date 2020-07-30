#!/usr/bin/env python3

def twoNumberSum(array, targetSum):
    # Write your code here.

    # O(nlog(n)) time | O(1) space
    '''
       using library sort functionality (like heap sort) will be (nlogn) time
       complexity. Same as solution one no variational variable memory is used. 
    '''
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
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
