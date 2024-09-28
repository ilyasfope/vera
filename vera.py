from os import system

# my text

text_login = """

BY = Natso Code

[1]- use feroxbuster
[2]- use subfinder
[3]- use sqlmap
[4]- exit

"""

while 1 > 0:
    print(text_login)

    choice = int(input("please choice a number : "))

# for feroxbuster tool

    def feroxbuster():

        url = input("please enter url for testing : ")

        word_list = input("please enter your word list : ")

        system("feroxbuster -u {} -w {}".format(url,word_list))

# for subfinder tool

    def subfinder():

        url = input("please enter url for testing : ")

        system("subfinder -d {}".format(url))

# for sqlmap tool

    def sqlmap():

        url = input("please enter url for testing : ")

        system(f"sqlmap -u {url} --banner --batch")

# for condition

    if choice == 1:

        feroxbuster()

    elif choice == 2:

        subfinder()
    
    elif choice == 3:

        sqlmap()

    elif choice == 4:
        break

    else:
        print("error try again")
        break


