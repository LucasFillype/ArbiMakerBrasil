import customtkinter as ctk
import tkinter as tk


Apostas_Dia = []
Casas_apostas = ["Pinnacle", "NoviBet", "McGames", "BetVip", "Betano", "Stake"]
Valor_casas = ["R$5000", "R$2000", "R$3500", "R$1000","R$0", "R$0"]


def Lista_casas():
    while True:
        print(f"\nCasas:")
        for i, (casa, valor) in enumerate(zip(Casas_apostas, Valor_casas)):
            print(f"{i + 1} --> {casa} --> {valor}")

        print("\n=== [1] PARA ALTERAR VALOR ===")
        print("=== [0] PARA SAIR ===")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite apenas números.")
            continue

        if opcao == 1:
            try:
                escolha = int(input("Qual casa você quer alterar (número): "))
                if 1 <= escolha <= len(Casas_apostas):
                    novo_valor = input(f"Digite a nova banca da casa {Casas_apostas[escolha - 1]} (ex: R$3000): ")
                    Valor_casas[escolha - 1] = novo_valor
                    print("✅ Valor alterado com sucesso!\n")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Digite um número válido.")
        elif opcao == 0:
            print("Saindo... 👋")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        
        
# Função para registrar uma nova aposta
def registrar_apostas():
    print("\nCasas Disponíveis:")
    for i, casa in enumerate(Casas_apostas):
        print(f"{i + 1} --> {casa}")

    indice1 = int(input("Número da Casa 1: ")) - 1
    indice2 = int(input("Número da Casa 2: ")) - 1

    aposta = {
        "numero": int(input("Número da Aposta: ")),
        "data": input("Data do jogo: "),
        "hora": input("Horário do jogo: "),
        "casa1": Casas_apostas[indice1],
        "casa2": Casas_apostas[indice2],
        "stake1": float(input("Valor da stake 1: ")),
        "stake2": float(input("Valor da stake 2: ")),
        "odd1": float(input("Valor da odd 1: ")),
        "odd2": float(input("Valor da odd 2: "))
    }

    aposta["lucro"] = (aposta["stake1"] * aposta["odd1"]) - aposta["stake1"] - aposta["stake2"]
    aposta["lucro_porcentagem"] = (aposta["lucro"] / (aposta["stake1"] + aposta["stake2"])) * 100

    Apostas_Dia.append(aposta)

    print(f"\nLucro da Aposta: R${aposta['lucro']:.2f}")
    print(f"{aposta['lucro_porcentagem']:.2f}%")

# Função para visualizar todas as apostas com resumo
def ver_apostas():
    print("\n📋 Todas as apostas registradas:")
    if not Apostas_Dia:
        print("Nenhuma aposta registrada ainda.")
    else:
        for i, aposta in enumerate(Apostas_Dia, 1):
            resumo = (
                f"{i}. Aposta {aposta['numero']} | "
                f"{aposta['casa1']} vs {aposta['casa2']} | "
                f"Data: {aposta['data']} às {aposta['hora']} | "
                f"Stake1: R${aposta['stake1']} @ {aposta['odd1']} | "
                f"Stake2: R${aposta['stake2']} @ {aposta['odd2']} | "
                f"Lucro: R${aposta['lucro']:.2f} | "
                f"{aposta['lucro_porcentagem']:.2f}%"
            )
            print(resumo)

        print(f"[1]== Lucro do Dia ==")
        print(f"[0]== Voltar ==")
        opcao = int(input("Escolha uma opção"))
        if opcao == 1:
                lucro_dia = 0
                for ap in Apostas_Dia:
                    lucro_dia = lucro_dia + ap["lucro"]
                print(f"\n💰 Lucro do dia: R${lucro_dia:.2f}")
        elif opcao == 0:
         print("Voltando...")

# Função para apagar uma aposta
def apagar_aposta():
    ver_apostas()
    if not Apostas_Dia:
        return

    try:
        numero = int(input("Digite o número da aposta que deseja apagar: ")) - 1
        if 0 <= numero < len(Apostas_Dia):
            aposta_removida = Apostas_Dia.pop(numero)
            print(f"Aposta removida com sucesso:\nAposta {aposta_removida['numero']}")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")

def Metas_semana():
    meta_semanal = "R$900"
    print(f"Meta Semanal = {meta_semanal}")
    lucro_dia = 0
    for ap in Apostas_Dia:
            lucro_dia = lucro_dia + ap["lucro"]  
    diferenca_meta = (lucro_dia - 900)
    print(f"\nFaltam == R${diferenca_meta} Para Bater a meta ==")

    print(f"[1] Para Alterar a Meta Semanal")
    print(f"[0] Para voltar")

    opcao = int(input("Digite sua opção:"))
    if opcao == 1:
        nova_meta = input("Digite a nova meta (ex: R$1000): ")
        meta_semanal = {nova_meta}
        print(f"\n✅ Nova meta definida: {meta_semanal}")
        
    elif opcao == 0:
        print("saindo...")



# HUB / Menu Principal
while True:
    print("\n=== MENU PRINCIPAL ===")
    print("[1] Registrar nova aposta")
    print("[2] Ver todas as apostas")
    print("[3] Apagar alguma aposta")
    print("[4] Ver Casas de Apostas")
    print("[5] Metas da Semana")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_apostas()
    elif opcao == "2":
        ver_apostas()
    elif opcao == "3":
        apagar_aposta()
    elif opcao == "4":
        Lista_casas()
    elif opcao == "5":
        Metas_semana()

    elif opcao == "0":
        print("Saindo... 👋")
        break
    else:
        print("Opção inválida. Tente novamente.")