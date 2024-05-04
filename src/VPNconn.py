import subprocess
import time

class VPNConnector:
    def __init__(self):
        self.vpn_process = None

    def start_vpn(self):
        print("Iniciando conexão VPN...")
        try:
            # Inicia o processo VPN
            self.vpn_process = subprocess.Popen(["/snap/bin/riseup-vpn.launcher"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(5)  # Aguarda alguns segundos para que a conexão VPN seja estabelecida
            print("Conexão VPN estabelecida com sucesso.")
        except Exception as e:
            print(f"Erro ao iniciar a conexão VPN: {e}")

    def stop_vpn(self):
        print("Encerrando conexão VPN...")
        if self.vpn_process:
            try:
                # Termina o processo VPN
                self.vpn_process.terminate()
                self.vpn_process = None
                print("Conexão VPN encerrada.")
            except Exception as e:
                print(f"Erro ao encerrar a conexão VPN: {e}")
        else:
            print("Não há conexão VPN ativa.")

if __name__ == "__main__":
    vpn_connector = VPNConnector()
    while True:
        print("\nEscolha uma opção:")
        print("1. Iniciar VPN")
        print("2. Parar VPN")
        print("3. Sair")

        choice = input("Opção: ")

        if choice == "1":
            vpn_connector.start_vpn()
        elif choice == "2":
            vpn_connector.stop_vpn()
        elif choice == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

"""
outlook:
┌──(eduardo㉿eduardor)-[~/repos/A-Nony/src]
└─$ python VPNconn.py

Escolha uma opção:
1. Iniciar VPN
2. Parar VPN
3. Sair
Opção: 1
Iniciando conexão VPN...
Conexão VPN estabelecida com sucesso.

Escolha uma opção:
1. Iniciar VPN
2. Parar VPN
3. Sair
Opção: 3
Saindo...
"""