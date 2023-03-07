import os
from time import sleep
from colorama import Fore


#CHOOSE COLOR YOU WANT (RED, YELLOW, GREEN, BLUE, CYAN, MAGENTA)
color = 'BLUE' 

#Set to 'true' if you want the light version of your selected color
lightcolor = 'false' 

#Set to what you want the titlebar to say
title = 'IP Pinger'  

#https://patorjk.com/software/taag/  - This site is used to make 3d text 
#https://www.asciiart.eu - ascii artwork
bannertext = """
██████╗ ██╗███╗   ██╗ ██████╗ ███████╗██████╗  
██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝██╔══██╗ 
██████╔╝██║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝ 
██╔═══╝ ██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗ 
██║     ██║██║ ╚████║╚██████╔╝███████╗██║  ██║ 
╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""




def main():
    os.system('cls||clear')
    os.system(f'title {title}')
    a = getattr(Fore, color)
    if lightcolor == 'true': a = getattr(Fore, f"LIGHT{color}_EX")
    else:a = getattr(Fore, color)
    print(f"""{a}{bannertext}{Fore.RESET} """)
    
    hostname = input(f"[ {a}+{Fore.RESET} ] IP Address: ")
    while True:
        try:
         print(a)
         response = os.system("ping " + hostname + ' -t')
        except: 
           main()
            
main()
