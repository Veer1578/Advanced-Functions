number = int(input('Enter a number: '))
num = [x for x in range(0, number + 1) if x%2==1]
print(f'All the odd numbers till the number you gave are {num}')

fruits = ['apple', 'banana', 'guava', 'mango']
new_list = [x[0].upper()+x[1:] for x in fruits]
print(new_list)