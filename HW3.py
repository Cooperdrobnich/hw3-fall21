# Your name: Cooper Drobnich
# Your student id: 8426 6316
# Your email: Drobnich@umich.edu
# List who you have worked with on this homework: Adam Brenner and Samer Yassir


# import the random module for use in this program
import random

# Create the class Crystal_Ball
 # create the constructor (__init__) method
    # it takes as input: a list of possible predictions
    # it takes as input: a list of possible names
    # it sets this object's prediction_list (instance variable) to the passed list of possible predictions
    # it sets this object's name_list (instance variable) to the passed list of possible names
    # it sets this object's prediction_history_list (instance variable) to an empty list
    # it sets this object's name_history_list (instance variable) to an empty list

    # create the __str__ method
    # It should return a string with all the predictions
    # in prediction_list separated by commas

    # create the predict method that takes a name
    # it randomly picks an index from 0 to the number of items in the prediction_list minus one
    # it adds that index to the end of the prediction_history_list
    # it randomly picks an index from 0 to the number of items in the name_list minus one
    # it adds that index to the end of the name_history_list
    # It adds the passed name to the end of the name_list
    # it returns a string with the prediction at the picked index followed by the name at the name index

    # create the check_name method that takes a name
    # it checks if the name is in the name_list and if so returns
    #         "I already have that name!”
    # Otherwise it returns the prediction from predict

    # create the print_history method
    # prints "[prediction index] prediction - [name index] name" for each of the indices in the prediction_history_list
    # from the first to the last with each on a single line.  If there are not items in the
    # prediction_history_list it prints "None yet"
    # it does not return anything!

    # EXTRA POINTS
    # create the most_frequent method
    # it takes as input:
    #    a number, n. Ex: 200
    # it generates a random response n times by calling predict.
    # It prints the counts for each prediction index, and
    # prints the most frequently occurring prediction index and prediction
class Crystal_Ball:

    def __init__(self, prediction_list, name_list):
        self.prediction_list = prediction_list
        self.name_list = name_list
        self.prediction_history_list = []
        self.name_history_list = []
        
    def __str__(self):
        return str(self.prediction_list)
          

    def predict(self, name):
        the_prediction_index = random.randrange(0, len(self.prediction_list) - 1)
        self.prediction_history_list.append(the_prediction_index)
        the_name_index = random.randrange(0, len(self.name_list) - 1)
        self.name_history_list.append(the_name_index) 
        self.name_list.append(name)
        return str(self.prediction_list[the_prediction_index]) + str(self.name_list[the_name_index])

    def check_name(self, name):
        if name in self.name_list:
            return "I already have that name!"
        else:
            return self.predict(name)

    def print_history(self):
        v1 = self.prediction_history_list
        v2 = self.name_history_list
        if len(self.prediction_history_list) == 0:
            print("None yet")
        for index in range(len(self.prediction_history_list)):

            print("[",v1[index],"]", self.prediction_list[v1[index]], " - ", "[", v2[index],"]", self.name_list[v2[index]])


def main():

    # Replace the prediction_list with your desired predictions!
    prediction_list = ["Is going to take a class with ",
                        "Will fall in love with ",
                        "Will spill on ",
                        "Must go on a walk with ",
                        "Is going to have a snowball fight with "]
    # Replace the name_list with your desired names!
    name_list = ['Yasmeen', 'Xinghui', 'Elaina', 'Anna', 'Ewelina', 'Nik']
    bot = Crystal_Ball(prediction_list, name_list)
    while True:
        get_name = input("type your first name or type 'quit' to exit: ")
        if get_name == "quit":
            print("exiting the statement")
            break
        print(bot.check_name(get_name))
    

        


    
        
    
        


    
    
    # get the first name or quit
    
    # loop while name is not "quit"

        # get the result from check_name

        # print name - result from check_name

        # get the next name or quit

def test():

    prediction_list = ["Is going to take a class with ",
                        "Will fall in love with ",
                        "Will spill on ",
                        "Must go on a walk with ",
                        "Is going to have a snowball fight with "]

    name_list = ['Yasmeen', 'Elaina', 'Anna', 'Ewelina', 'Nik']

    print()
    print("Testing Crystal Ball:")
    bot2 = Crystal_Ball(prediction_list, name_list)

    print("Testing the __str__ method")
    print(bot2)
    print()

    print("Printing the history when no predictions have been generated yet")
    bot2.print_history()
    print()

    print("Giving the name: Muna")
    print(bot2.check_name("Muna"))
    print()

    print("Giving the name: Muna again")
    print(bot2.check_name("Muna"))
    print()

    print("Giving the name: Mike")
    print(bot2.check_name("Mike"))
    print()

    print("Printing the history")
    bot2.print_history()
    print()

    print("Printing name_list")
    print(bot2.name_list)
    print()

    #EXTRA POINTS
    #Uncomment the lines below if you attempt the extra credit!
    # print("Testing most_frequent method")
    # print(bot2.most_frequent(1000))


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    test()
