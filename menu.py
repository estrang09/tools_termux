import time, os
from colaboradores import colabora
from update_upgrade import atualiza_sistema
from install_ferramentas import *
from info_sys import *


while True:
    Data = time.strftime("%d/%m/%Y")
    Hora = time.strftime("%H:%M:%S")
    print("=" * 60)
    print('{:^60}'.format("Data: " + Data + "  " "Hora: " + Hora))
    with open('banner_script.txt', 'r') as f:
        banner = f.read()
        print(banner)
    escolha = int(input("Escolha uma opção:\t\n>>> "))
    if escolha == 1:
        atualiza_sistema()
    elif escolha == 2:
        banner_ferramentas()
        valor = int(input("O que deseja instalar: "))
        if valor == 1:
            vim()
        elif valor == 2:
            python()
        elif valor == 3:
            netcat()
        elif valor == 4:
            nano()
        elif valor == 5:
            nmap()
        elif valor == 6:
            whois()
        elif valor == 7:
            figlet()
        elif valor == 8:
            git()
        elif valor == 9:
            curl()
        elif valor == 10:
            ruby()
        elif valor == 11:
            openvpn()
        elif valor == 12:
            tor_proxyschain()
        elif valor == 13:
            hydra()
        elif valor == 14:
            tsu_sudo()
        elif valor == 15:
            wget()
        elif valor == 0:
            sair_do_programa()
        else:
            print("Opção invalida!\n")
            break
    elif escolha == 3:
        banner_info_system()
        valor = int(input("==> Escolha uma opção: "))
        if valor == 1:
            sistema_operacional()
        elif valor == 2:
            usuario_atual()
        elif valor == 3:
            versao_kernel()
        elif valor == 4:
            data_do_mes()
        else:
            print("Opção invalida!\n")
            break
    elif escolha == 4:
        colabora()
    elif escolha == 5:
        print("Saindo do programa...")
        sleep(3)
        os.system("clear")
        break
    else:
        print("Opção invalida!")
        break