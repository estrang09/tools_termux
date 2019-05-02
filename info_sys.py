#######################################
"MOSTRA INFORMAÇÕES BASICAS DO SISTEMA"
#######################################
import os
import sys


def banner_info_system():
    menu_info_system= """
    [ 1 ] - Sistema operacional
    [ 2 ] - Usuário Atual
    [ 3 ] - Versão do Kernel
    [ 4 ] - Data
    [ 0 ] - Sair do programa\n"""

    print(menu_info_system)


def sistema_operacional():
    command = os.popen("uname -a").read()
    mensagem = ("Sistema operacional rodando é: {}".format(command))
    print(mensagem)
def usuario_atual():
    command = os.popen("whoami").read()
    mensagem = ("O usuário atual é: {}".format(command))
    print(mensagem)
def versao_kernel():
    command = os.popen("uname -r").read()
    mensagem = ("Versão atual do kernel: {} ".format(command))
    print(mensagem)
def data_do_mes():
    command = os.popen("date").read()
    mensagem = ("Data atual é: {} ".format(command))
    print(mensagem)
