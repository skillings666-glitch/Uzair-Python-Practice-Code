# importing the os module which is necassary for file i/o in this program
import os

# importing colorama module that is used for colorizing the output of program
from colorama import Fore, Style, init

# initializing colorama
init(autoreset=True)

# predefining the colors for easy use
red = Fore.RED + Style.BRIGHT
grn = Fore.GREEN + Style.BRIGHT
yel = Fore.YELLOW + Style.BRIGHT
cyn = Fore.CYAN + Style.BRIGHT



# This function Scans a folder and all its subfolders, printing the name of every file it finds.
def explore(path, level=0):
    if os.path.isdir(path):                 # this checks if it is folder or not
        items = os.listdir(path)            # this stores contents present in the folder into a list
        for item in items:                  # this loop iterates through all the items present in the folder
            try:                            # try-except block to handle errors
                indent = '  ' * level                # this makes the indentation pattern for better presentation
                full_path = os.path.join(path, item) # Creates the full path of item so function can explore it.
                print(yel + indent + f'[FOLDER] {item}')          # this prints the folder name with its indent
                explore(full_path, level + 1)               # THIS IS THE RECURSIVE CALL
            except PermissionError:         # try-except block to handle errors
                print(red + f'[PERMISSION ERROR] {item}')
    elif os.path.isfile(path):                  # this checks if the given path is already a file
        cpath = path.split('/')[-1]             # this makes the path clean by only retaining the file name
        print(cyn + f'[FILE] {cpath}')                # this prints the file name


# main function
def main():
    # asking the user to input the path of the directory to list its contents
    path = input(grn + 'Enter the path:')
    # calling explore function
    explore(path)


# calling the main function
if __name__ == '__main__':
    main()
