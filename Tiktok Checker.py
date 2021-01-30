import random, string, requests, time
from colorama import Fore
from discord_webhook import DiscordWebhook
import os
os.system("cls" or "clear")
print(Fore.RED+"""

Discord Server :  https://discord.gg/eJeHG7D6pm
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

hmletters = int(input('how many letters you want to check : '))
print("")
#wbhook = input("Webhook url : ")
print()
time.sleep(.3)


while True:
    usernames = ('').join(random.choices(string.ascii_lowercase + string.digits, k=hmletters))
    #webhook = DiscordWebhook(url=wbhook, content=f'`{usernames}` | Might be Available or Banned on => ||`{webss}`|| |')
    r = requests.get(f'https://m.tiktok.com/node/share/user/@{usernames}')
    responsecode = r.json()['statusCode']
    
    if responsecode == 10202:
        print(Fore.CYAN + "[+] " + Fore.GREEN + "Available" + Fore.WHITE + ' |=>' + Fore.LIGHTMAGENTA_EX + f' {usernames}'+Fore.WHITE+" <=|" + Fore.CYAN + " [+]")
        f = open("availables.txt", "a", encoding='utf-8')
        f.write(f"{usernames} | Might be Available or Banned|\n")
        #webhook.execute()
    elif responsecode == 10222:
        print(Fore.CYAN+"[-] "+Fore.RED + "UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {usernames}'+Fore.WHITE+" <=|"+Fore.CYAN+" [-]")
    elif responsecode == 0:
        print(Fore.CYAN+"[-] "+Fore.RED + "UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {usernames}'+Fore.WHITE+" <=|"+Fore.CYAN+" [-]")
    elif responsecode == 10221:
        print(Fore.CYAN+"[-] "+Fore.RED + "Banned"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {usernames}'+Fore.WHITE+" <=|"+Fore.CYAN+" [-]")
    elif responsecode == 10223:
        print(Fore.CYAN+"[-] "+Fore.RED + "Banned"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {usernames}'+Fore.WHITE+" <=|"+Fore.CYAN+" [-]")
    else:
        print(Fore.CYAN+"[X] "+Fore.WHITE+f"i cant find {usernames}'s statusCode !!' "+Fore.CYAN+" [X]"+Fore.WHITE)
