###############################################
"FAZ A INSTALAÇAO DAS FERRAMENTAS SELECIONADAS"
###############################################
import os
from time import sleep



################################################
"COMANDO PARA FICAR LIMPANDO A TELA QUANDO NECES"
"SARIO"
################################################
limpador = os.system("clear")


def banner_ferramentas():
	banner_tools = """[ 1 ] - Vim
[ 2 ] - Python		[ 10 ] - Ruby
[ 3 ] - Netcat		[ 11 ] - Openvpn	
[ 4 ] - Nano		[ 12 ] - Tor e Proxyschain
[ 5 ] - Nmap		[ 13 ] - Hydra
[ 6 ] - Whois		[ 14 ] - Tsu(sudo)
[ 7 ] - Figlet		[ 15 ] - Wget
[ 8 ] - Git		[ 0 ] - Sair do programa
[ 9 ] - Curl
"""
	print(banner_tools)

def vim():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S vim")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nVim instalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador

def python():
		limpador
		sleep(3)
		mensagem = "Por favor aguarde !"
		print(mensagem)
		comando_programa = os.system("pacman -S python")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nPython instalado com sucesso!\n E pronto para o uso!\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def netcat():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S netcat")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nNetcatinstalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def nano():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S nano")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nNano instalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def nmap():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S nmap")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nNmap instalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def whois():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S whois")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nWhois instalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def figlet():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S figlet")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nFiglet instalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def git():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S git")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nGit instalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def curl():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S curl")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nCurl instalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def ruby():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S ruby")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nRuby instalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def openvpn():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S openvpn")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nOpenvpn instalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def tor_proxyschain():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S figlet")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nFiglet instalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def hydra():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S hydra")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nHydra instalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def tsu_sudo():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S tsu")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nTsu(sudo) instalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def wget():
		limpador
		sleep(3)
		mensagem = '\nPor favor aguarde !\n\n\n'
		print(mensagem)
		sleep(3)
		limpador
		comando_programa = os.system("pacman -S wget")
		if comando_programa == 0:
			limpador
			sleep(3)
			print("\nWget instalado com sucesso!\n E pronto para o uso !\n")
			sleep(3)
			limpador
		else:
			limpador
			sleep(3)
			print("\nOps meu parça algo deu errado!\n")
			sleep(3)
			limpador
def sair_do_programa():
	limpador
	sleep(3)
	mensagem = '\nPor favor aguarde ...\n\n\n'
	print(mensagem)
	sleep(3)
	limpador
	sleep(3)
	saindo = '\nSaindo do programa ...\n\n\n'
	print(saindo)
	limpador
	saida = exit()