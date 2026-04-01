# A simple calculator that does calculation using only python's arithemathic operators

user_input = int(input('What type of calculations do you want to do? \nMake sure that you use the symbols correctly. \n1. Addition + \n2. Multiplication * \n3. Division / \n4. modulus % \n5. Subtraction - \n6. Raised to power ** \nSelect: '))


if user_input == 1:
    print('This is how your calculations will look like...2 + 100')
    add_input1 = int(input('Enter the first number: '))
    add_input2 = int(input('Enter the second number: '))
    print(f'{add_input1} + {add_input2} = {add_input1 + add_input2}')
elif user_input == 2:
    print('This is how your calculations will look like...2 * 100')
    mul_input1 = int(input('Enter the first number: '))
    mul_input2 = int(input('Enter the second number: '))
    print(f'{mul_input1} x {mul_input2} = {mul_input1 * mul_input2}')   
elif user_input == 3:
    print('This is how your calculations will look like...2 / 100')
    div_input1 = int(input('Enter the first number: '))
    div_input2 = int(input('Enter the second number: '))
    print(f'{div_input1} / {div_input2} = {div_input1 / div_input2}')
elif user_input == 4:
    print('This is how your calculations will look like...2 % 100')
    mol_input1 = int(input('Enter the first number: '))
    mol_input2 = int(input('Enter the second number: '))
    print(f'{mol_input1} % {mol_input2} = {mol_input1 % mol_input2}')    
elif user_input == 5:
    print('This is how your calculations will look like...2 - 100')
    sub_input1 = int(input('Enter the first number: '))
    sub_input2 = int(input('Enter the second number: '))
    print(f'{sub_input1} - {sub_input2} = {sub_input1 - sub_input2}')
elif user_input == 6:
    print('This is how your calculations will look like...2 ^ 100')
    rai_input1 = int(input('Enter the first number: '))
    rai_input2 = int(input('Enter the second number: '))
    print(f'{rai_input1} ^ {rai_input2} = {rai_input1 ** _input2}')
else:
    print('Invalid input! Choose from the given selections.')
       