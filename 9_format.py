name = 'Dug'
age = 20
print('I am ' + name + ' and I am ' + str(age) + ' years old.')
print('I am {} and I am {} years old.'.format(name, age))
print('I am {1} and I am {0} years old.'.format(name, age))
print('I am {0} and I am {1} years old. I really am named {0}'.format(name, age))
print('I am {name} and I am {years} years old. '.format(name=name, years=age))

funds = 150.81722
print('Finds : {}'.format(funds))
print('Finds : {:f}'.format(funds))
print('Finds : {:.1f}'.format(funds))
print('Finds : {:10.1f}'.format(funds))
print('Finds : {:>10.1f}'.format(funds))
print('Finds : {:<10.1f}'.format(funds))
print('Finds : {:^10.1f}'.format(funds))
print('Finds : {:-^10.1f}'.format(funds))
