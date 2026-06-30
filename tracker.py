
# Imports

import storage as dt
import functions as fc

# ----------------------------------------------------------------------

pesos = dt.load_pesos()
profile = dt.load_profile()
if not profile:
    print("Perfil vazio. Vamos preencher algumas informações.")
    profile = fc.create_profile(profile)
    dt.save_profile(profile)

# Menu principal
while True:

    print("\n===== HYpertrophy Tracker =====")
    print("1. Adicionar novo peso")
    print("2. Ver histórico de pesos")
    print("3. Ver estatísticas")
    print("4. Perfil do usuário")
    print("5. Sair")
    opc = input("Escolha uma opção (1-5): ")

    if opc == "1":
        while True:
            entrada = input("Digite o novo peso em kg: ")
            novo_peso = fc.check_peso(entrada)

            if novo_peso is None:
                print("Entrada inválida. Por favor digite um número positivo (ex: 61.2).")
                continue

            break

        reg = fc.create_reg(novo_peso)
        pesos.append(reg)
        dt.save_pesos(pesos)
        print("Peso adicionado com sucesso!")

    elif opc == "2":
        fc.show_history(pesos)
    elif opc == "3":
        fc.show_stats(pesos, profile)
    elif opc == "4":
        while True:
            print("\n===== Perfil do Usuário =====")
            print("1. Ver perfil")
            print("2. Editar perfil")
            print("3. Voltar ao menu principal")
            sub_opc = input("Escolha uma opção (1-3): ")
            if sub_opc == "1":
                fc.show_profile(profile)
            elif sub_opc == "2":
                profile = fc.edit_profile(profile)
                dt.save_profile(profile)
            elif sub_opc == "3":
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção entre 1 e 3.")
    elif opc == "5":
        print("Fechando... até amanhã!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")

# -------------------------------------------------------