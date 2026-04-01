# A programme that can generate different multiplication tables



what_type = int(input('Which number do you want to generate its multiplication table? '))


how_many = int(input(f'How many times do you want the table to reach? \nNote: If you choose 8 times, the table will run seven times! '))

for how_many in range(1, how_many):
    print(f'{what_type} x {how_many} = {what_type * how_many}')

