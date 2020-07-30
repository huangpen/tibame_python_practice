def debug(case, test, correct):
  if correct == str(test):
    print('Success!')
  else:
    print('Fail')
    print('\tYour output: {}'.format(test))             
    print('\tCorrect output: {}'.format(correct))                  
    print('\n\tInput(s): {}\n'.format(case))                          
