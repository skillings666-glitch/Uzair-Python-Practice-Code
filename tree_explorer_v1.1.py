import os
from colorama import Fore, Style, init

init(autoreset=True)

red = Fore.RED + Style.BRIGHT
grn = Fore.GREEN + Style.BRIGHT
yel = Fore.YELLOW + Style.BRIGHT
cyn = Fore.CYAN + Style.BRIGHT

def explore(path, level=0):
    if os.path.isdir(path): 
        items = os.listdir(path) 
        for item in items: 
            try:       
                indent = '  ' * level   
                full_path = os.path.join(path, item) 
                print(yel + indent + f'[FOLDER] {item}') 
                explore(full_path, level + 1)    
            except PermissionError: 
                print(red + f'[PERMISSION ERROR] {item}')
    elif os.path.isfile(path):        
        cpath = path.split('/')[-1]    
        print(cyn + f'[FILE] {cpath}')   

def main():
    path = input(grn + 'Enter the path:')
    explore(path)

if __name__ == '__main__':
    main()
