classes = []
print('How many classes are you taking this semester?')
numOfClasses=int(input())
for i in range(0,numOfClasses):
    subject=input('Enter the name of the class: ')
    classes.append(subject)
print('The classes you are taking are:')
for sub in classes:
    print(sub)