import csv
import string
import datetime
import itertools
import time

class passwordStrength:

    def __init__(self, password, rating):
        self.password = password
        self.rating = rating

    def commonPasswords(self):
        with open("common_passwords.csv") as f: #opening excel spreadsheet of 5000 most common words and passwords
            reader = csv.reader(f)
            commonWords = list(reader)

            passwordList = [self.password]

            if passwordList in commonWords: # if user password is in spreadsheet
                self.rating = self.rating - 100 #lose 100 points
                print("-100 points, common password")
                print(self.rating)

            else:
                self.rating = self.rating + 10
                print("Not a common password, + 10!")
                print(self.rating)

    def passwordLen(self):
        lengthPass = len(self.password) #giving out points depending on length of password
        print("Password Length: " + str(lengthPass))
        if lengthPass < 4:
            self.rating = self.rating - 50
            print("Password much too short, -50")

        elif lengthPass < 7:
            self.rating = self.rating - 25
            print("Password too short, -25")

        elif lengthPass < 10:
            self.rating = self.rating + 1
            print("Password fine length, +1 point")

        else:
            self.rating = self.rating + 25
            print("Password a good length, + 25  ")

        print(self.rating)

    def complexity(self):
        specialCharacters = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "@", "'", "#", "~", "?", "/", "<", ">"]
        count = 0 #giving out points for use of special characteds
        holder = 0
        for x in specialCharacters:
            if specialCharacters[holder] in self.password:
                count = count + 1
            holder = holder + 1

        if count > 0:
            print("+10 for use of special charater")
            self.rating = self.rating + 10
        else:
            print("-10 for not using special character")
            self.rating = self.rating - 10

        print("OVERALL SCORE: " + str(self.rating))
        print("Please wait 10 seconds for password cracking to commence.")

class passwordCracker:
    def __init__(self, password):
        self.password = password
        self.characters = []
        self.passwordLength = len(password)

    def characterFinder(self):
        letters = string.printable
        letters = [char for char in letters]


        start = time.time()

        with open("common_passwords.csv") as f: #cracking password using a dictionary attack
            reader = csv.reader(f)
            commonWords = list(reader) #putting common passwords in a list

            passwordList = [self.password]
            print(passwordList)
            counter = 0
            found = False
            start = time.time()
        for i in range(len(commonWords)):  #looping through common passwords
            lengthOfList = len(commonWords)
            if commonWords[i] == passwordList: #if passwords match
                print("password cracked: " + self.password)
                end = time.time()
                print(f"Password cracked in {end - start}") #print message
                found = True
                break #break from for loop

            else:
                counter = counter + 1
                if counter == lengthOfList: #if end of list reached
                    break #break from for loop





        # passwordSplit = [char for char in self.password]
        passwordTuple = tuple(self.password)
        count = 0
        checker = 0
        if found == False:
            for i in range(0, len(letters)+1):
                for x in itertools.permutations(letters, i): #every combination of all letters on a keyboard
                    if found == False:


                        count=count+1
                        print(count)

                        passwordTuple = list(passwordTuple)
                        print(passwordTuple)
                        variable = list(x)
                        print(variable)

                        checker = checker + 1
                        if checker == 20000: #using 20,000 test runs to create an estimated time to crack password
                            #based on power of computer and speed it takes to go through 20,000 loops
                            holderTime = time.time()
                            averageTime = holderTime - start
                            worstCase = pow(104, self.passwordLength) #iterates through all possible combinations
                            bestCase = pow(104, self.passwordLength - 1) #first combination of length
                            averageCase = (bestCase + worstCase) / 2 #difference between both
                            worstCase = (worstCase * averageTime)/20000 #time taken per iteration
                            bestCase = (bestCase * averageTime)/20000
                            averageCase = (averageCase * averageTime)/20000
                            print("Longest time to crack: " + str(datetime.timedelta(seconds=worstCase))) #converting seconds
                            #into hour: min: seconds format
                            print("Shortest time to crack " + str(datetime.timedelta(seconds=bestCase)))
                            #if overflow error is displayed, it means that it will take over 10,000 days...
                            print("Average time to crack " + str(datetime.timedelta(seconds=averageCase)))
                            time.sleep(7)

                        if passwordTuple == variable:
                        # if collections.Counter(passwordTuple) == collections.Counter(x):
                            print("password cracked: " + self.password)
                            end = time.time()
                            seconds = end - start
                            endTime = datetime.timedelta(seconds=seconds)
                            print(f"Password cracked in {endTime}")  # print message
                            print("Longest time to crack: " + str(datetime.timedelta(seconds=worstCase)))
                            print("Shortest time to crack " + str(datetime.timedelta(seconds=bestCase)))
                            print("Average time to crack " + str(datetime.timedelta(seconds=averageCase)))
                            found = True

                            break  # break from for loop







print("The aim of the game. You start with 0 points, the higher number you end up on the stronger your password!")
print("Good luck ;)")
password = input("Please enter the tested password: ")

test1 = passwordStrength(password, 0)
test1.commonPasswords()
test1.passwordLen()
test1.complexity()
time.sleep(10)
test2 = passwordCracker(password)
test2.characterFinder()