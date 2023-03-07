import os
import re
from time import sleep
from colorama import Fore


# CHOOSE COLOR YOU WANT (RED, YELLOW, GREEN, BLUE, CYAN, MAGENTA)
color = 'BLUE' 

# Set to 'true' if you want the light version of your selected color
lightcolor = 'false' 

# Set to what you want the titlebar to say
title = 'IP Pinger'  

# https://patorjk.com/software/taag/  - This site is used to make 3d text 
# https://www.asciiart.eu - ascii artwork
bannertext = """
██████╗ ██╗███╗   ██╗ ██████╗ ███████╗██████╗  
██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝██╔══██╗ 
██████╔╝██║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝ 
██╔═══╝ ██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗ 
██║     ██║██║ ╚████║╚██████╔╝███████╗██║  ██║ 
╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

def is_valid_ipv4_address(ip_address):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip_address) is not None


def main():
    os.system('cls||clear')
    os.system(f'title {title}')
    a = getattr(Fore, color)
    if lightcolor == 'true':
        a = getattr(Fore, f"LIGHT{color}_EX")
    else:
        a = getattr(Fore, color)
    print(f"""{a}{bannertext}{Fore.RESET} """)

    hostname = input(f"[ {a}+{Fore.RESET} ] IP Address: ")
    if not is_valid_ipv4_address(hostname):
        print(f"[ {Fore.RED}-{Fore.RESET} ] Invalid IP address")
        sleep(2)
        main()

    while True:
        try:
            print(a)
            response = os.system("ping " + hostname + ' -t')
        except:
            main()

main()
