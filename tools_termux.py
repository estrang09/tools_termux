#coding:utf-8

import os
from time import sleep

print("\33[34m================================")
print("""\33[33m[1] - Atualizar o sistema
[2] - Git
[3] - Nano
[4] - Wget
[5] - Tsudo(sudo)
[6] - Nmap
[7] - Tor e Proxchains
[8] - Metasploit
[9] - Figlet
[10] - Vim
[11] - Hydra
\33[m""")
print("\33[34m===============================")

usr = int(input("\33[32mQual opcao desejada: \33[32m"))

if usr == 1:
	os.system("apt-get update && apt-get upgrade -y")
	os.system("clear")
	print("Sistema atualizado com sucesso!!!")
	sleep(5)
	os.system("clear")
elif usr == 2:
	os.system("apt-get install git -y")
	os.system("clear")
	print("Git instalado com sucesso!!!")
	sleep(5)
	os.system("clear")
elif usr == 3:
	os.system("apt-get install nano -y")
	os.system("clear")
	print("Nano instalado com sucesso!!!")
	sleep(5)
	os.system("clear")
elif usr == 4:
	os.system("apt-get install wget -y")
	os.system("clear")
	print("Wget instalado com sucesso!!!")
	sleep(5)
	os.system("clear")
elif usr == 5:
	os.system("apt-get install tsu -y")
	os.system("clear")
	print("Tsudo instalado com sucesso!!!")
	sleep(5)
	os.system("clear")
elif usr == 6:
	os.system("apt-get install nmap -y")
	os.system("clear")
	print("Nmap instalado com sucesso!!!")
	sleep(5)
	os.system("clear")
elif usr == 7:
	os.system("apt-get install tor -y && apt-get install proxychains -y")
	os.system("clear")
	print("Tor e Proxychains instalados com sucesso")
	sleep(5)
	os.system("clear")
elif usr == 8:
	os.system("git clone https://github.com/estrang09/Metasploit.git")
	sleep(8)
	os.system("cd Metasploit && bash metasploit.sh")
	os.system("clear")
	print("Metasploit instalado com sucesso!!!")
	sleep(5)
	os.system("clear")
elif usr == 9:
	os.system("apt-get install figlet -y")
	os.system("clear")
	print("Figlet instalado com sucesso!!!")
	sleep(5)
	os.system("clear")
elif usr == 10:
	os.system("apt-get install vim -y")
	os.system("clear")
	print("Vim instalado com sucesso!!!")
	sleep(5)
	os.system("clear")
elif usr == 11:
	os.system("apt-get install hydra -y")
	os.system("clear")
	print("Hydra instalado com sucesso!!!")
	sleep(5)
	os.system("clear")
	