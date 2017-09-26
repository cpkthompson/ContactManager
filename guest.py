class MESTGuest:

    guest_list = {'Charles':'charles.thompson@meltwater.org'}


    def add_guest(self):
        name = input("Enter name: ")
        email = input("Enter email: ")
        self.guest_list[name] = email

    def return_guest_email(self):
        name = input("Enter name to retrieve email: ").strip()
        for key in self.guest_list:
            if key == name:
                print (self.guest_list[key])
            else:
                print ("Not found")
                
        





if __name__ == '__main__':
    new_guest = MESTGuest()
    # new_guest.add_guest()
    new_guest.return_guest_email()