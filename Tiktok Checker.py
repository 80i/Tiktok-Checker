import requests, time, sys, os, concurrent.futures
from colorama import Fore
from discord_webhook import DiscordWebhook
os.system("cls" or "clear")
print(Fore.RED+"""

Discord Server :  https://discord.gg/HWdgMvFFdY
        My discord : @K4Sp3r#1337

 _________  _   __      _________       __              ______  __                    __                     
|  _   _  |(_) [  |  _ |  _   _  |     [  |  _        .' ___  |[  |                  [  |  _                 
|_/ | | \_|__   | | / ]|_/ | | \_|.--.  | | / ]      / .'   \_| | |--.  .---.  .---.  | | / ] .---.  _ .--.  
    | |   [  |  | '' <     | |  / .'`\ \| '' <       | |        | .-. |/ /__\\/ /'`\] | '' < / /__\\[ `/'`\] 
   _| |_   | |  | |`\ \   _| |_ | \__. || |`\ \      \ `.___.'\ | | | || \__.,| \__.  | |`\ \| \__., | |     
  |_____| [___][__|  \_] |_____| '.__.'[__|  \_]      `.____ .'[___]|__]'.__.''.___.'[__|  \_]'.__.'[___]    
                                                                                                             

    Made By : K4Sp3r
     Insta : @K4S 
      Snap : Fuun
"""+Fore.WHITE)
time.sleep(.5)
print("")
print()
time.sleep(.3)
def checker(usernames):
    try:
        r = requests.get(f'https://m.tiktok.com/node/share/user/@{usernames}')
        responsecode = r.json()['statusCode']
        
        if responsecode == 10202:
            print(Fore.CYAN + "[+] " + Fore.GREEN + "Available" + Fore.WHITE + ' |=>' + Fore.LIGHTMAGENTA_EX + f' {usernames}'+Fore.WHITE+" <=|" + Fore.CYAN + " [+]")
            f = open("availables.txt", "a", encoding='utf-8')
            f.write(f"{usernames} | Might be Available |\n")
        elif responsecode == 10222:
           print(Fore.CYAN+"[-] "+Fore.RED + "UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {usernames}'+Fore.WHITE+" <=|"+Fore.CYAN+" [-]")
           f = open("taken.txt", "a", encoding='utf-8')
           f.write(f"{usernames} \n")
        elif responsecode == 10225:
            print(Fore.CYAN+"[-] "+Fore.RED + "UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {usernames}'+Fore.WHITE+" <=|"+Fore.CYAN+" [-]")
            f = open("taken.txt", "a", encoding='utf-8')
            f.write(f"{usernames} \n")
        elif responsecode == 0:
            print(Fore.CYAN+"[-] "+Fore.RED + "UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {usernames}'+Fore.WHITE+" <=|"+Fore.CYAN+" [-]")
            f = open("taken.txt", "a", encoding='utf-8')
            f.write(f"{usernames} \n")
        elif responsecode == 10221:
            print(Fore.CYAN+"[-] "+Fore.RED + "Banned"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {usernames}'+Fore.WHITE+" <=|"+Fore.CYAN+" [-]")
            f = open("banned.txt", "a", encoding='utf-8')
            f.write(f"{usernames} \n")
        elif responsecode == 10223:
            print(Fore.CYAN+"[-] "+Fore.RED + "Banned"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {usernames}'+Fore.WHITE+" <=|"+Fore.CYAN+" [-]")
            f = open("banned.txt", "a", encoding='utf-8')
            f.write(f"{usernames} \n")
        else:
            print(Fore.CYAN+"[X] "+Fore.WHITE+f"i cant find {usernames} 's statusCode !!' "+Fore.CYAN+" [X]"+Fore.WHITE)
            f = open("unknown.txt", "a", encoding='utf-8')
            f.write(f"{usernames} \n")
    except:
        pass


with open('usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f]
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(checker, usernames)
