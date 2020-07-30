#!/usr/bin/env python3

def twoNumberSum(array, targetSum):
    # Write your code here.

    # O(n^2) time | O(1) space
    ''' Double for loop, quadratic run time
        No variables increase as the input size increases,
        therefore constant space complexity.
    '''
    for i in range(len(array) - 1):
	firstNum = array[i]		
	for j in range(i + 1, len(array)):
            secondNum = array[j]
	    if firstNum + secondNum == targetSum:
		return [firstNum, secondNum]
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
