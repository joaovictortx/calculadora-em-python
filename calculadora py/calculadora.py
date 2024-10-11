# Funções para operações básicas
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

# Função principal
def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolha = input("Escolha uma operação (1/2/3/4): ")

        # Verifica se a escolha é válida
        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")

            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")

            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

            elif escolha == '4':
                resultado = dividir(num1, num2)
                print(f"{num1} / {num2} = {resultado}")

            # Pergunta ao usuário se deseja continuar
            continuar = input("Deseja fazer outra operação? (s/n): ")
            if continuar.lower() != 's':
                break
        else:
            print("Opção inválida! Tente novamente.")

# Iniciar calculadora
if __name__ == "__main__":
    calculadora()
