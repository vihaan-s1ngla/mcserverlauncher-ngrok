import os
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
from sys import platform
import linecache as lc
import subprocess
from pathlib import Path
import time
import shutil
from installation import *

#Methods
def firstTimeChecker():
    path_to_file = 'programconf.txt'
    path = Path(path_to_file)
    if path.is_file():
        startprogram()
    else:
        info()
        print("PLEASE INPUT REQUIRED DATA!")
        time.sleep(1)
        installngrok()
        editconf_noquit()
        startoverallserver()

def menu():
    print("[1] Start Server")
    print("[2] Edit Config")
    print("[3] Information")
    print("[0] Quit The Program")

def info():
    os.system("clear")
    print("NOTE: THIS PRODUCT WILL INSTALL PREREQUISITES! THESE INCLUDE:\n            - NGROK\n            - SEVERAL PYTHON LIBARIES, LOOK AT REQUIREMENTS.TXT TO LEARN!\n      PLEASE ALSO MAKE SURE YOU HAVE A MINECRAFT SERVER ALREADY DOWNLOADED, THIS CANNOT INSTALL THE SERVER FOR YOU BECAUSE OF MOJANG'S EULA.")
    print()
    columns = shutil.get_terminal_size().columns
    print("=====================================================================".center(columns))    
    time.sleep(4)
    print()
    print("Welcome to a minecraft server launcher that DOES NOT require port forwarding!")
    time.sleep(4)
    print("All this software requires is the path to the start file of the server, and the URL to your webhook! (don't mess these paths/urls up, otherwise it will not work!)")
    time.sleep(4)
    print("If you do mess it up, fret not, you can edit the issue in the 'Edit Config' module in the main menu.")
    time.sleep(4)
    print("Enjoy!")
    time.sleep(1)
    os.system("clear")

def editconf():
    os.system("clear")
    f = open('programconf.txt', 'w+')
    pathtomcserver = input("Path to minecraft server start file: ")
    f.write("Path To Minecraft Server: \n")
    f.write(pathtomcserver)
    print("Path Saved.")
    f.write("\n")
    outputdiscordwebhook = input("Discord Webhook URL: ")
    f.write("\n")
    f.write("Discord Webhook: \n")
    f.write(outputdiscordwebhook)
    print("Discord Webhook Saved")
    quit()

def editconf_withclear():
    os.system("clear")
    f = open('programconf.txt', 'w+')
    pathtomcserver = input("Path to minecraft server start file: ")
    f.write("Path To Minecraft Server: \n")
    f.write(pathtomcserver)
    print("Path Saved.")
    f.write("\n")
    outputdiscordwebhook = input("Discord Webhook URL: ")
    f.write("\n")
    f.write("Discord Webhook: \n")
    f.write(outputdiscordwebhook)
    print("Discord Webhook Saved")
    os.system("clear")

def editconf_noquit():
    os.system("clear")
    f = open('programconf.txt', 'w+')
    pathtomcserver = input("Path to minecraft server start file: ")
    f.write("Path To Minecraft Server: \n")
    f.write(pathtomcserver)
    print("Path Saved.")
    f.write("\n")
    outputdiscordwebhook = input("Discord Webhook URL: ")
    f.write("\n")
    f.write("Discord Webhook: \n")
    f.write(outputdiscordwebhook)
    print("Discord Webhook Saved")

def startngrokserver():
    webhookfromconfigfile = lc.getline('programconf.txt', 5).strip()
    webhook = DiscordWebhook(url = webhookfromconfigfile)

    subprocess2 = subprocess.Popen("ngrok tcp 25565 -region au", shell=True, stdout=subprocess.PIPE)
    subprocess1 = subprocess.Popen("curl -s localhost:4040/api/tunnels", shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess1.stdout.read()
    returnedIP = json.loads(subprocess_return)["tunnels"][0]["public_url"][6:]
    print(returnedIP)
    embed = DiscordEmbed(title='BOYS IMORTAL IS RECORDING', color='FF0000')
    embed.add_embed_field(name='JOIN UP AT', value=returnedIP)

    webhook.add_embed(embed)
    response = webhook.execute()

def startminecraftserver():
    mcserverpathfromconfigfile = lc.getline('programconf.txt', 2).strip()
    os.system(mcserverpathfromconfigfile)

def startoverallserver():
        startngrokserver()
        startminecraftserver()

def startprogram():
    os.system("clear")
    menu()
    option = int(input("Enter your option: "))

    while option != 0:
        if option == 1:
            startoverallserver()
            quit()
        elif option == 2:
            #Do option 2 ting
            editconf()
            quit()
        elif option == 3:
            info()
        else:
            print("Invalid Option.")

        print()
        menu()
        option = int(input("Enter your option: "))

#Program
firstTimeChecker()