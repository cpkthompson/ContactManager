class Contact():
	"""Class for saving a new contact 
	provided by the user through user input."""

	def __init__(self):
		self.name = str(input("Enter your name: \n"))
		self.phone_number = int(input("Enter your phone number: \n"))
		self.gender = str(input("Enter your gender: \n"))
		self.email_address = str(input("Enter your email address: \n"))
		self.postal_address = str(input("Enter your postal address: \n"))


new_contact = Contact()

print("**************************************")
print("Your name is: {}".format(new_contact.name))
print("Your phone number is: {}".format(new_contact.phone_number))
print("Your gender is: {}".format(new_contact.gender))
print("Your email address is: {}".format(new_contact.email_address))
print("Your postal address is: {}".format(new_contact.postal_address))