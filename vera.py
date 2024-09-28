from os import system
from colorama import * # type: ignore

init()

# my text

green = Fore.GREEN
red = Fore.LIGHTRED_EX
reset = Style.RESET_ALL


text_login = f"""

{Fore.LIGHTCYAN_EX}BY = Natso Code

you must download these tools on your device.

{green}[1]- feroxbuster: {reset}find hidden paths folders and files in the site.
{green}[2]- subfinder: {reset}helps detect subdomains on the site.
{green}[3]- sqlmap: {reset}sql injection vulnerability scanning.
{green}[4]- nikto: {reset}site vulnerability scanning.
{green}[5]- whois: {reset}get information about the site.
{green}[6]- exit: {reset}in order to exit the program.

"""
# for check input

def check_input(input):

    if input == "" or input.strip() == False or input.isdigit():

        print(red + "sorry write something appropriate")
    
# for input url

def url_input():

    return input("please write the site you want to check : ")

while 1 > 0:

    print(text_login)

    choice = int(input("choose a number to get started ==> "))

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

# for nikto tool

    def nikto():

        url = url_input()

        check_input(url)

        system("nikto -h {}".format(url))

# for whois

    def whois():

        url = url_input()

        check_input(url)

        system(f"whois {url}")

# for condition

    if choice == 1:

        feroxbuster()
    

    elif choice == 2:

        subfinder()
    
    elif choice == 3:

        sqlmap()

    elif choice == 4:

        nikto()

    elif choice == 5:

        whois()

    elif choice == 6:

        print(Fore.LIGHTGREEN_EX + "successfully exited")

        break

    else:

        print(Fore.RED + "there is an error in the program,try again.")

        break


