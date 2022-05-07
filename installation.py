import os
from sys import platform

def installngrok():
        authtoken = input("Please input your ngrok AUTHTOKEN: ")
        os.system("ngrok authtoken " + authtoken)