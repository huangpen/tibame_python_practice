#!/usr/bin/env python3

def isValidSubsequence(array, sequence):
    # Write your code here.

    # O(n) time | O(1) space - where n is the length of the array
    '''
    Using for loop instead.
    '''
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)





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
        value = isValidSubsequence(case['array'], case['sequence'])
        debug_v1.debug(case, value, correct_output[count])
