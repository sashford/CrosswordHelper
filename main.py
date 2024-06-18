# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from WordHelper import WordHelper

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wordlist = WordHelper()
    exit = False
    while not exit:
        pattern = input("\n\nType in pattern you would like to search for.  Type \"\help\" for help.\n")

        if pattern == "\help":
            print("Type in the letters you know and use the \"_\" character for letters you don't know.\n")
            print("Type \"\quit\" to exit the program.")

        elif pattern == "\quit":
            print("\nExiting Program")
            exit = True
        else:
            print("Possible words:")
            for word in wordlist.parse(pattern):
                print("    " + word)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
