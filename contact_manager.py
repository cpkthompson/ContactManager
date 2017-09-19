# Exercise 3: More ContactManager

# Take Your code from Exercise 2...
# * Create a ContactManager that manages a list of Contacts.
# * Create a loop that prompts to either add a contact, delete a contact or search for contact by name
# * Commit early + often; push your code to GitLabBucketHub

class Contact:
	"""Class for saving a new contact 
	provided by the user through user input."""

	def __init__(self):
		self.name = str(input("Enter your name: \n"))
		# self.phone_number = int(input("Enter your phone number: \n"))
		# self.gender = str(input("Enter your gender: \n"))
		# self.email_address = str(input("Enter your email address: \n"))
		# self.postal_address = str(input("Enter your postal address: \n"))




class ContactManager:
	"""
		The ContactManager has a phonebook, which we can list all the contacts in, 
		add new contacts to, search and delete alreadty added contacts.
	"""

	def __init__(self, phonebook=[]):
		self.phonebook = phonebook
	
	def all_contacts(self):
		for contact in self.phonebook:
			print (contact)

	def add_contact(self):
		contact = Contact()
		self.phonebook.append(contact)

	def delete_contact(self):
		pass

	def search_contact(self):
		pass

		
		
number = ContactManager()
number.add_contact()

