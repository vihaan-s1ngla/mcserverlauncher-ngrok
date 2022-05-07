import os
from sys import platform

def installngrok():
    if platform == "linux" or platform == "linux2":
        # linux
        print("yuh")
    elif platform == "darwin":
        # OS X
        print("yuh")
    elif platform == "win32":
        authtoken = input("Please input your ngrok AUTHTOKEN: ")
        os.system("ngrok authtoken " + authtoken)