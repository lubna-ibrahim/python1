class LoginSystem:
    def __init__(self, correct_password, max_attempts=3):
        self.correct_password = correct_password
        self.max_attempts = max_attempts
        self.attempts = 0

    def authenticate(self):
        while self.attempts < self.max_attempts:
            password = input("Enter password: ")
            if password == self.correct_password:
                print("Welcome to the system!")
                return True
            else:
                self.attempts += 1
                print("Wrong Password!")
                
        print("Too many failed attempt123456s. Access locked!")
        return False

# Main Program
if __name__ == "__main__":
    login_system = LoginSystem(correct_password="123456789")
    login_system.authenticate()
