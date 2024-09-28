from os import system

# my text

text_login = """

BY = Natso Code

[1]- use feroxbuster
[2]- use subfinder
[3]- use sqlmap
[4]- exit

"""
# for check input

def check_input(input):
    if input == "" or input.strip() == False or input.isdigit():
        print("sorry write something appropriate")
    
# for input url

def url_input():
    return input("please enter url for testing : ")

while 1 > 0:
    print(text_login)

    choice = int(input("please choice a number : "))

# for feroxbuster tool

    def feroxbuster():

        url = url_input()

        word_list = input("please enter your word list : ")

        check_input(url)

        check_input(word_list)

        system("feroxbuster -u {} -w {}".format(url,word_list))

# for subfinder tool

    def subfinder():

        url = url_input()

        check_input(url)

        system("subfinder -d {}".format(url))

# for sqlmap tool

    def sqlmap():

        url = url_input()

        check_input(url)

        system(f"sqlmap -u {url} --banner --batch")

# for condition

    if choice == 1:

        feroxbuster()
    

    elif choice == 2:

        subfinder()
    
    elif choice == 3:

        sqlmap()

    elif choice == 4:
        print("exit is success")
        break

    else:
        print("error try again")
        break


