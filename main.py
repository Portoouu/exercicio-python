def opcao_1():
    print("Você escolheu a opção 1.")

def opcao_2():
    print("Você escolheu a opção 2.")

def opcao_3():
    print("Você escolheu a opção 3.")

def exibir_menu():
    print("Escolha uma opção:")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Opção 3")
    print("0. Sair")
    
    escolha = int(input("Digite o número da opção desejada: "))
    return escolha

# Função principal que executa o programa
def main():
    while True:
        escolha = exibir_menu()
        
        if escolha == 1:
            opcao_1()
        elif escolha == 0:
            print("Saindo do programa.")
            break
        elif escolha == 2:
            opcao_2()
        elif escolha == 3:
            opcao_3()
        else:
            print("Opção inválida. Escolha um número válido.")

if __name__ == "__main__":
    main()
