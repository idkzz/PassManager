import sys
import colorama
import random
import time
import string
from colorama import Fore



colorama.init(autoreset=True)

print("")
print("")

name_program = str(input(Fore.GREEN + " What name you want to save for this password : "))

if type(name_program) == str:
    print("\n")
    print(Fore.GREEN + " Saved as " + name_program + " !")
    print(Fore.GREEN + " Do you want generate a random password or create your own?")
    print("\n")
    print(Fore.GREEN + " 1.Create")
    print(Fore.GREEN + " 2.Generate")
    print("\n")

    option = int(input(Fore.GREEN + " Option : "))

    if option == 1:

        print(Fore.GREEN + "\n You choosed option 1!\n")
        password = input(Fore.GREEN + " What password will you save : ")

        file = open('passwords.txt', 'a')
        file.write(name_program + " -> " + password + "\n\n")
        file.close()
        
        print("")
        print(Fore.GREEN + " Done!")
        print(Fore.GREEN + " Exiting...")
        time.sleep(2)
        exit(0)

    elif option == 2:

        print(Fore.GREEN + "\n You choosed option 2!\n")
        
        #
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!()/&%"

        password_length = int(input(Fore.GREEN + " Password length: "))
        print(Fore.GREEN + " Generating the password!\n")
        time.sleep(2)

        
        for pwd in range(1):
            final_password = ''
            for number_chact in range(password_length):
                final_password += random.choice(characters)
            
            print(Fore.GREEN + " Password generated : " + final_password + "\n")
            
            file = open('passwords.txt', 'a')
            file.write(name_program + " -> " + final_password + "\n\n")
            file.close()
        #                         
        print(Fore.GREEN + " Generated!")
        print(Fore.GREEN + " Exiting...")
        time.sleep(2)
        exit(0)


else :
    print(" ")
    print(Fore.GREEN + " Error 404 Program!")
