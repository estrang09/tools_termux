###########################################################
"IRÁ DAR UM UPGRADE E UPDATE DENTRO DO SISTEMA OPERACIONAL"
###########################################################
import os
from functools import partial
from time import sleep


def atualiza_sistema():
	mensagem = "\nPor favor aguarde!\nSistema sendo atualizado!"
	print(mensagem)
	sleep(4)
	limpa_tela  = os.system("clear")
	

	mensagem_comando = 'Comando sendo executado! Aguarde o término'
	print(mensagem_comando)
	sleep(3)
	comando = os.system("pacman -Syu")

	if comando == 0:
		termino_mensagem = 'Seu foi atualizado corretamente!\n'
		print(termino_mensagem)
		sleep(3)
		limpa_tela = os.system("clear")
	else:
		mensagem_else = '\nOps ! Algo deu errado meu parça!'
		print(mensagem_else)
		sleep(3)
		limpa_tela = os.system("clear")
