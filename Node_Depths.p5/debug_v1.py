import json

def debug(case, test, correct):
  if correct == test:
    print('Success!')
  else:
    print('Fail')
    print('\tYour output: {}'.format(test))             
    print('\tCorrect output: {}'.format(correct))
    printpretty = json.dumps(case, indent=4, sort_keys=True)
    print('\n\tInput(s): \n{}\n'.format(printpretty))                          
