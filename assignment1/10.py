class User():
    def __init__(self, first_name, last_name,user_name, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.location = location
    def describe_user(self):
        print(f"Name: {self.first_name + " " + self.last_name}\nUsername: {self.user_name}\nEmail: {self.email}\nLocation: {self.location}")
    def greet_user(self):
        print(f'Welcome back {self.user_name}!')
