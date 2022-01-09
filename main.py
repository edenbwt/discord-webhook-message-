from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
import colorama
from colorama import Fore
import os
import time

banner = (Fore.LIGHTBLUE_EX + """
              .andAHHAbnn.
           .aAHHHAAUUAAHHHAn.
          dHP^~"        "~^THb.
    .   .AHF                YHA.   .
    |  .AHHb.              .dHHA.  |
    |  HHAUAAHAbn      adAHAAUAHA  |
    I  HF~"_____        ____ ]HHH  I
   HHI HAPK""~^YUHb  dAHHHHHHHHHH IHH
   HHI HHHD> .andHH  HHUUP^~YHHHH IHH
   YUI ]HHP     "~Y  P~"     THH[ IUP
    "  `HK                   ]HH'  "
        THAn.  .d.aAAn.b.  .dHHP
        ]HHHHAAUP" ~~ "YUAAHHHH[
        `HHP^~"  .annn.  "~^YHH'
         YHb    ~" "" "~    dHF
          "YAb..abdHHbndbndAP"
           THHAAb.  .adAHHF
            "UHHHHHHHHHHU"
              ]HHUUHHHHHH[
            .adHHb "HHHHHbn.
     ..andAAHHHHHHb.AHHHHHHHAAbnn..
.ndAAHHHHHHUUHHHHHHHHHHUP^~"~^YUHHHAAbn.
  "~^YUHHP"   "~^YUHHUP"        "^YUP^"
╔╦╗  ┌┬┐┌─┐┌─┐┌─┐  ┌┐ ┌─┐┌┬┐ 
 ║║───│ ├─┤├┤ ├┤   ├┴┐│ │ │ 
═╩╝   ┴ ┴ ┴└  └    └─┘└─┘ ┴ 
        by eden
""")

def main():
    print(banner)
    start = input(Fore.WHITE + '[' + Fore.GREEN + "1" + Fore.WHITE + '] ' + "send message\n" + Fore.WHITE + '[' + Fore.GREEN + "2" + Fore.WHITE + '] ' + "send embed\n=>")

    if start == "1":
        message = input(Fore.WHITE + '[' + Fore.GREEN + "+" + Fore.WHITE + ']' + 'your message : ')
        webhook = DiscordWebhook(url='your Webhook', content=message)
        webhook.execute() 
        print(Fore.WHITE + '[' + Fore.YELLOW + "-" + Fore.WHITE + ']' + 'message send !')
        time.sleep(1.5)
        os.system('cls')
        main()
    if start == "2":
        webhook = DiscordWebhook(url='your Webhook', username="Captain Devoir")
        cours = input(Fore.WHITE + '[' + Fore.GREEN + "+" + Fore.WHITE + ']' +"description veux tu donner : ")
        prof = input(Fore.WHITE + '[' + Fore.GREEN + "+" + Fore.WHITE + ']' +"quells profs de la journer : ")
        Heure = input(Fore.WHITE + '[' + Fore.GREEN + "+" + Fore.WHITE + ']' +"quells Heures de la journer : ")
        jours = input(Fore.WHITE + '[' + Fore.GREEN + "+" + Fore.WHITE + ']' +"quells jours de la journer : ")
        Matier = input(Fore.WHITE + '[' + Fore.GREEN + "+" + Fore.WHITE + ']' +"quells matier de la journer : ")
        
        embed = DiscordEmbed(title='Cours de la journer', description=cours, color=242424)
        embed.set_author(name='Author Name', url='https://github.com/edenbwt', icon_url='https://avatars.githubusercontent.com/u/94796854?s=96&v=4')
        embed.set_footer(text='Embed Footer Text')
        embed.set_timestamp()
        embed.add_embed_field(name='prof', value=prof)
        embed.add_embed_field(name='Heure', value=Heure)
        embed.add_embed_field(name='jours', value=jours)
        embed.add_embed_field(name='Matier', value=Matier)
        webhook.add_embed(embed)
        response = webhook.execute()
        print(Fore.WHITE + '[' + Fore.YELLOW + "-" + Fore.WHITE + ']' + 'embed send !')
        time.sleep(1.5)
        os.system('cls') 
        main()
        
if __name__ == "__main__":
    main()
    
