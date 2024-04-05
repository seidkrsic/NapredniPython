""" 
Users: Make a class called User. Create two attributes called 
first_name and last_name, and then create several other attributes 
that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s 
information. Make another method called greet_user() that prints a 
personalized greeting to the user.
Create several instances representing different users, 
and call both meth- ods for each user.
"""

class User: 
    def __init__(self,first_name, last_name, email): 
        self.first_name = first_name
        self.last_name = last_name 
        self.email = email 
        self.login_attempts = 0 

    def increment_login_attempts(self): 
        self.login_attempts += 1 
    
    def restart_login_attemts(self): 
        self.login_attempts = 0 
    
    def describe_user(self): 
        print(f"First name: {self.first_name}") 
        print(f"Last name: {self.last_name}") 
        print(f"Email: {self.email}") 
    
    def greet_user(self): 
        print(f"Hello {self.first_name}! Welcome back!") 

first_name = input("First Name: ") 
last_name = input("Last Name: ") 
email = input("Email: ") 

user1 = User(first_name,last_name,email)  
print(user1.describe_user())
user1.greet_user()

