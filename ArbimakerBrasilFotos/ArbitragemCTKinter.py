import customtkinter as ctk

# Inicializando as listas
Apostas_Dia = []
Casas_apostas = ["Pinnacle", "NoviBet", "McGames", "BetVip", "Betano", "Stake"]
Valor_casas = ["R$5000", "R$2000", "R$3500", "R$1000", "R$0", "R$0"]

# Função para exibir as casas de apostas
def Lista_casas():
    casas_str = "\n".join([f"{casa} --> {valor}" for casa, valor in zip(Casas_apostas, Valor_casas)])
    casas_label.config(text=f"Casas:\n{casas_str}")

# Função para registrar uma nova aposta
def registrar_apostas():
    # Tela de entrada para a aposta
    registrar_window = ctk.CTkToplevel()
    registrar_window.title("Registrar Aposta")

    ctk.CTkLabel(registrar_window, text="Número da Aposta:").pack(padx=20, pady=5)
    numero_aposta = ctk.CTkEntry(registrar_window)
    numero_aposta.pack(padx=20, pady=5)

    ctk.CTkLabel(registrar_window, text="Data do Jogo:").pack(padx=20, pady=5)
    data_jogo = ctk.CTkEntry(registrar_window)
    data_jogo.pack(padx=20, pady=5)

    ctk.CTkLabel(registrar_window, text="Hora do Jogo:").pack(padx=20, pady=5)
    hora_jogo = ctk.CTkEntry(registrar_window)
    hora_jogo.pack(padx=20, pady=5)

    ctk.CTkLabel(registrar_window, text="Stake 1:").pack(padx=20, pady=5)
    stake1 = ctk.CTkEntry(registrar_window)
    stake1.pack(padx=20, pady=5)

    ctk.CTkLabel(registrar_window, text="Stake 2:").pack(padx=20, pady=5)
    stake2 = ctk.CTkEntry(registrar_window)
    stake2.pack(padx=20, pady=5)

    ctk.CTkLabel(registrar_window, text="Odd 1:").pack(padx=20, pady=5)
    odd1 = ctk.CTkEntry(registrar_window)
    odd1.pack(padx=20, pady=5)

    ctk.CTkLabel(registrar_window, text="Odd 2:").pack(padx=20, pady=5)
    odd2 = ctk.CTkEntry(registrar_window)
    odd2.pack(padx=20, pady=5)

    def salvar_aposta():
        aposta = {
            "numero": int(numero_aposta.get()),
            "data": data_jogo.get(),
            "hora": hora_jogo.get(),
            "casa1": Casas_apostas[0],  # Apenas exemplo, você pode adicionar um menu de seleção
            "casa2": Casas_apostas[1],  # Igual acima
            "stake1": float(stake1.get()),
            "stake2": float(stake2.get()),
            "odd1": float(odd1.get()),
            "odd2": float(odd2.get())
        }
        aposta["lucro"] = (aposta["stake1"] * aposta["odd1"]) - aposta["stake1"] - aposta["stake2"]
        aposta["lucro_porcentagem"] = (aposta["lucro"] / (aposta["stake1"] + aposta["stake2"])) * 100

        Apostas_Dia.append(aposta)

        print(f"\nLucro da Aposta: R${aposta['lucro']:.2f}")
        print(f"{aposta['lucro_porcentagem']:.2f}%")
        registrar_window.destroy()

    ctk.CTkButton(registrar_window, text="Salvar Aposta", command=salvar_aposta).pack(padx=20, pady=20)

# Função para ver todas as apostas
def ver_apostas():
    apostas_str = "\n".join([f"Aposta {aposta['numero']} | {aposta['casa1']} vs {aposta['casa2']} | Lucro: R${aposta['lucro']:.2f}" for aposta in Apostas_Dia])
    apostas_label.config(text=f"Apostas Registradas:\n{apostas_str}")

# Função para apagar uma aposta
def apagar_aposta():
    apagar_window = ctk.CTkToplevel()
    apagar_window.title("Apagar Aposta")

    ctk.CTkLabel(apagar_window, text="Número da Aposta para Apagar:").pack(padx=20, pady=5)
    numero_aposta = ctk.CTkEntry(apagar_window)
    numero_aposta.pack(padx=20, pady=5)

    def remover_aposta():
        try:
            numero = int(numero_aposta.get()) - 1
            if 0 <= numero < len(Apostas_Dia):
                aposta_removida = Apostas_Dia.pop(numero)
                print(f"Aposta removida: Aposta {aposta_removida['numero']}")
                apagar_window.destroy()
            else:
                print("Número inválido.")
        except ValueError:
            print("Digite um número válido.")

    ctk.CTkButton(apagar_window, text="Remover Aposta", command=remover_aposta).pack(padx=20, pady=20)

# Função para exibir o menu principal
def abrir_menu():
    menu_window = ctk.CTk()
    menu_window.title("Menu Principal")

    ctk.CTkButton(menu_window, text="Registrar Nova Aposta", command=registrar_apostas).pack(padx=20, pady=10)
    ctk.CTkButton(menu_window, text="Ver Apostas", command=ver_apostas).pack(padx=20, pady=10)
    ctk.CTkButton(menu_window, text="Apagar Aposta", command=apagar_aposta).pack(padx=20, pady=10)
    ctk.CTkButton(menu_window, text="Ver Casas de Apostas", command=Lista_casas).pack(padx=20, pady=10)
    ctk.CTkButton(menu_window, text="Sair", command=menu_window.quit).pack(padx=20, pady=10)

    global casas_label
    casas_label = ctk.CTkLabel(menu_window, text="")
    casas_label.pack(padx=20, pady=10)

    global apostas_label
    apostas_label = ctk.CTkLabel(menu_window, text="")
    apostas_label.pack(padx=20, pady=10)

    menu_window.mainloop()

# Iniciar o programa com o menu principal
abrir_menu()