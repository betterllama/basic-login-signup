#log in process
def login():
	Username = input("Enter Username : ")
	if Username == 'betterllama' or NewUsername:
			Password = input("Enter Password : ")
	else:
		print("Username Incorrect")
	if Password == 'omoshi' or NewPassword:
		print("Welcome, " + Username)
	else:
		print("Password is incorrect") 
#sign up + log in process
def signup(NewUsername = 'default', NewPassword = 'default'):
	NewUsername = input("Choose a Username : ")
	NewPassword = input("Choose a Password : ")
	print("Would you like to log in now?")
	x = input("Type 'yes' or 'no' : ")
	if x == 'yes':
		Username = input("Enter Username : ")
		if Username == 'betterllama' or NewUsername:
			Password = input("Enter Password : ")
		else:
			print("Username Incorrect")
		if Password == 'omoshi' or NewPassword:
			print("Welcome, " + Username)
		else:
			print("Password is incorrect") 
	else:
		print("done")
#start sequence
def start():
	print("Would you like to Login or Sign Up? ")
	x = input("Type 'login' or 'signup' : ")
	if x == 'login':
		login()
	else:
		signup()
start()


	
