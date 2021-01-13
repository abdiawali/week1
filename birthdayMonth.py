#this program asks users their name and date of birth
# if it's users birth month it's display 'happy birhday month'
#it also tells users the length of their names.

from datetime import date

print('What is your name? ')
name=input()    #store users name

print('what month were you born? ')
dob=input()     #store users birthday month

print('Hello '+ name)
now=date.today() #today's date
this_month=now.strftime('%B')   #gets month as 'january' now.month=1
if dob.lower()==this_month.lower():      #sets month to lower and checks if the month is january
    print('Happy birthday month!')

print(f'there are {len(name)} letters in your name')    #tells users length of their name