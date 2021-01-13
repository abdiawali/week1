print('What is your name? ')
name=input()

print('what month were you born? ')
dob=input()

print('Hello '+ name)
month='august'
if dob.lower()==month:
    print('Happy birthday month!')

print('there are '+ str(len(name))+ ' letters in your name')