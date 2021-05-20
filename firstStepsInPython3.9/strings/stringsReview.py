"""
Create a function called username_generator take two inputs, first_name and last_name and returns a username.
The username should be a slice of the first three letters of their first name and the first four letters
of their last name.
If their first name is less than three letters or their last name is less than four letters it should
use their entire names.
For example, if the employee’s name is Abe Simpson the function should generate the username AbeSimp.
"""

def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name

"""
Create function password_generator so that it takes one input, username and in it define an empty string named password.
Inside password_generator create a for loop that iterates through the indices username by going from 0 to len(username).
To shift the letters right, at each letter the for loop should add the previous letter to the string password.
"""
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i - 1]
    return password


