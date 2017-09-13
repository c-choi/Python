# while True:
#    print('Who are you?')
#    name = input()
#    if name != 'Joe':
#        continue
#    print('Hello Joe, What is the password? (it is a fish.)')
#    password = input()
#    if password == 'swordfish':
#        break
#print('Access granted.')

name = ''
while not name:
    print('Enter you name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough room for all of your guests')
print('Done')
