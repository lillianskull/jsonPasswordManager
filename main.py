# Password Manager (Beginner Project)
# Obviously not intended to be used as an actual password manager, simply made as a beginner project since I started Python a day ago!

# Basically appending user data to a JSON file with a CLI.

import os
import json

from colorama import Fore
from colorama import Style

from platform import system as os_name

template = {
    'name': 'John',
    'passwordToSave': '123abc',
    'forPlatform': 'Facebook',
    'key': '{}'
}

toSave = {

}

readData = {

}

os_name = os_name()

def clear():
    if os_name == "Darwin" or os_name == "Linux":
        os.system("clear")
    elif os_name == "Windows":
        os.syste("cls")

def saveData(dataToSave: dict):
    listObj = []

    with open("data/user_data.json") as file:
        listObj = json.load(file)

    listObj.append(dataToSave)
    
    with open("data/user_data.json", 'w') as json_file:
        json.dump(listObj, json_file, indent = 4)

def findData(passedKey: str):
    with open('data/user_data.json', 'r') as openfile:
        newJson = json.load(openfile)

        for x in newJson:
            for key, value in x.items():
                if key == "key" and value == passedKey:
                    readData.update(x)

        openfile.close()

    return readData


def main():
    print(f"{Fore.LIGHTRED_EX}JSON{Style.RESET_ALL} Password Manager made with {Fore.YELLOW}Python{Style.RESET_ALL}\n\n")
    readOrWrite = input("Are you going to read or write a password?\nAnswer: ")

    if readOrWrite == "read":
        key = input("Give me the key you used to store the password!\nAnswer: ")
        
        dataReceived = findData(key)

        if dataReceived != None:
            print("Found your data.")

            name = dataReceived.get("name")
            password = dataReceived.get("password")
            platform = dataReceived.get("forPlatform")

            print(f"Name: {name}\nPassword: {password}\nPlatform: {platform}")

    elif readOrWrite == "write":
        name = input("What is your name?\nAnswer: ")
        password = input("What password are you saving?\nAnswer: ")
        platform = input(f"For which platform is \'{password}\' going to be used for?\nAnswer: ")
        key = input("You need a special key to secure it! What will it be?\nAnswer: ")

        newData = {
            'name': name,
            'password': password,
            'forPlatform': platform,
            'key': key
        }

        toSave.update(newData)
        prompt = input(f"Is this correct?\n{toSave}\n[n] [y]:")

        if prompt  == "n":
            print("Sorry! Reverting.")
            toSave.update(template)
        elif prompt == "y":
            print("Okay!\n")
            saveData(toSave)
        

if __name__ == "__main__":
    clear()
    main()