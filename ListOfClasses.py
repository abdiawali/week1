#this program asks users number of classes they take 
#then asks them to enter
#then displays list of classes one per line
classes = []    # empty lsit
print('How many classes are you taking this semester?')
numOfClasses=int(input())   #stores number of classes
for i in range(0,numOfClasses):
    subject=input('Enter the name of the class: ')
    classes.append(subject)     #adds each class to the classes list
print('The classes you are taking are:')
for sub in classes:
    print(sub)  #prints each list