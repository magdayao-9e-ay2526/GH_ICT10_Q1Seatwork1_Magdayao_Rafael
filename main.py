#All About Me
from pyscript import display, document


#String
name = "Rafael Sancho A. Magdayao"
#Integer
age = 15
#Float
height = 163.39
#List
country_list = ['Norway', 'Switzerland', 'Canada']
#Boolean
student_type = False
#Dictionary
fun_facts = {'color':'blue', 'car_brand':'Nissan', 'shoe_size':'9', 'best_friend':'Athena'}
#Set
favorite_fruits = set(['Apple', 'Banana', 'Pear', 'Cherry', 'Grape'])
#Tuple
days_of_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

display(f'Hello! My name is {name}. I am {age} years old. I am {height} cm tall.', target='info')
display(f'New Student?: {student_type}', target='new-student')
display(f'Fun Facts: {fun_facts}', target='new-student')
display(f'Favorite Fruits: {favorite_fruits}', target='new-student')
display(f'Days of the Week: {days_of_week}', target='new-student')