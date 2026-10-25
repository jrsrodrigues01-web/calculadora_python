import math

# Funções para cada operação
 
def mostrar_menu():
    print("\n" + "="*35)
    print("      CALCULADORA SIMPLIFICADA      ")
    print("="*35)
    print("Selecione a operação desejada:")
    print("[1] Adição (+)")
    print("[2] Subtração (-)")
    print("[3] Multiplicação (*)")
    print("[4] Divisão (/)")
    print("[5] Potenciação (x^y^)")
    print("[6] Raiz Quadrada (√x)")
    print("[0] Sair")
    print("="*35)

# Função para realizar a operação selecionada

def calculadora():
    while True:
        mostrar_menu()
        escolha = input("Digite o número da operação desejada: ")

        if escolha == '0':
            print("Saindo da calculadora. Até logo!")
            break

# Operação principal que chama as funções de acordo com a escolha do usuário 

        elif escolha in ['1', '2', '3', '4', '5', '6']:
            try:
                if escolha == '6':
                    num1 = float(input("Digite o número para calcular a raiz quadrada: "))
                    resultado = math.sqrt(num1)
                    print(f"Resultado: √{num1} = {resultado}")
                else:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))

                    if escolha == '1':
                        resultado = num1 + num2
                        print(f"Resultado: {num1} + {num2} = {resultado}")
                    elif escolha == '2':
                        resultado = num1 - num2
                        print(f"Resultado: {num1} - {num2} = {resultado}")
                    elif escolha == '3':
                        resultado = num1 * num2
                        print(f"Resultado: {num1} * {num2} = {resultado}")
                    elif escolha == '4':
                        if num2 != 0:
                            resultado = num1 / num2
                            print(f"Resultado: {num1} / {num2} = {resultado}")
                        else:
                            print("Erro: Divisão por zero não é permitida.")
                    elif escolha == '5':
                        resultado = math.pow(num1, num2)
                        print(f"Resultado: {num1}^{num2} = {resultado}")
            except ValueError:
                print("Erro: Entrada inválida. Por favor, digite números válidos.")
        else:
            print("Opção inválida. Por favor, selecione uma operação válida.")

if __name__ == "__main__":
    calculadora()