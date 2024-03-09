import random
import string

print('Welcome to Ajay Internship Project of Random Password Generator.')

# Now create a user input that how many  characters the password should have.
length = int(input('Enter the length of password you want: '))

a = string.ascii_lowercase # This  will contain all lower case alphabets
b = string.ascii_letters # This will contain all letters like  upper and lower case alphabets
c =  string.digits # This will contain  all digits from 0-9
d = string.punctuation # This will contain  all special characters like !@#$%^&*()_+{}:"<>?/|

# Now  we are creating an empty list which will store our final password component wise
combine = a+b+c+d

# Now we define a  function which will choose randomly from above components and add
def generate_password(length):
    if (length <= 7 or length > 12):
        return "Password Length must be between 8  to 12 characters"
    x = random.sample(combine, length)
    return ''.join(x)

print("Your strongly recommendation password is:",generate_password(length))

    
    