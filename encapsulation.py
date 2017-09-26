#Create a method that lets you change password given the current password

class Secret:
    def __init__(self, secret, password):
        self.__secret = secret
        self.__password = password

    def get_secret(self, password):
        if password == self.__password:
            print ('The secret is: "{}"'.format(self.__secret))
            return self.__secret

    def change_password(self):
        __old_password = str(input("Enter your old password: "))
        if __old_password == self.__password:
            new_password = str(input("Enter your new password: "))
            self.__password = new_password
            print ("Password Changed Sucessfully")


if __name__ == '__main__':
    charles_secret = Secret("I am beautiful.", "ThePassword")
    charles_secret.get_secret("ThePassword")
    charles_secret.change_password()
