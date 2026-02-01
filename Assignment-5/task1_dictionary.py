"""
Create a Dictionary of Student Marks
Asks the user to input a student's name.
Retrieves and displays the corresponding marks.
If the student’s name is not found, display an appropriate message.
"""



student_details = {'Noah' : 85 , 'Amy' : 84 , 'Lily' : 94 , 'Jess' : 78 , 'Isla' : 87}

try:
    name = input('Enter the student\'s name: ')
    print(f"{name}\'s marks : {student_details[name]}")
except KeyError:
    print("Student not found.")