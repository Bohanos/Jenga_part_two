# A programme that lists even or odd numbers between two ranges inputted by the user.

user_input = int(input('What type of numbers would you want to list? \n\2 1. Even \n\2 2. Odd \nSelect: '))
if user_input == 1:
    even_start = int(input('Input the start of the range '))
    even_end = int(input('Input the end of the range '))
    if even_start % 2 == 0:
        for i in range(even_start, even_end + 1, 2):        
            print(i)   
    elif even_start % 2 != 0:
        new_start = even_start + 1
        for i in range(new_start, even_end + 1, 2):
            print(i)
    else:
        print('Wrong input!')               
elif user_input == 2:   
    odd_start = int(input('Input the start of the range '))
    odd_end = int(input('Input the end of the range '))
    if odd_start % 2 == 1:
        for i in range(odd_start, odd_end + 1, 2):
            print(i)
    elif odd_start % 2 != 1:
        for i in range(odd_start + 1, odd_end + 1, 2):
            print(i) 
    else:
        print('Invalid input. Reselect') 
else:
    print('Invalid input. Rerun the code!') 

