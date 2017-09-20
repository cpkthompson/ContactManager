class Person:
    def __init__(self):
        self.name = str(input('Enter your name: '))
        self.nationality = str(input('Enter your nationality: '))
        

class EITs(Person):
    def __init__(self, name = "Charles", nationality = "Ghanaian"):
        super().__init__(name, nationality)
        
    def recite_fun_fact(self, fun_fact = "Likes dancing"):
        self.fun_fact = fun_fact
        print(self.fun_fact)


class Fellows(Person):
    def __init__(self, name = "Francis", nationality = "Ghanaian", happiness_level = "0"):
        super().__init__(name, nationality)
        self.happiness_level = happiness_level

    def eat(self):
        self.happiness_level = self.happiness_level + 1

    def teach(self):
        self.happiness_level = self.happiness_level - 1

        
class School:
    def __init__(self):
        fellows = Fellows()
        eits = EITs()

    def recruit(self):
        
        recruit_countries = ['Ghana', 'Kenya', 'Nigeria', 'South Africa', 'Ivory Coast']

        with open("eits.csv","r") as file_handler:
            for eit_details in file_handler.readlines():

                # eit_detail in eits.csv: Charles,Ghana

                eit = eit_details.split(",")
                if eit[1].strip() not in recruit_countries:
                    print ("Hello {}, \nMEST isn't recruiting from {} yet."
                        "\nThanks.\n".format(eit[0], eit[1].strip()))

    
if __name__ == '__main__':
    start_school = School()
    
    start_school.recruit()