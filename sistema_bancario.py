class Cliente:
    def _init_(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Conta:
    def _init_(self, cliente):
        self.agencia = "0001"
        self.numero = 1
        self.cliente = cliente
        self.saldo = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido!")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        elif valor > 500:
            print("Limite de saque é R$ 500!")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido!")

    def mostrar_extrato(self):
        print("\n=== EXTRATO ===")
        if not self.extrato:
            print("Não há movimentações.")
        else:
            for item in self.extrato:
                print(item)
        print(f"Saldo: R$ {self.saldo:.2f}")


# -------- PROGRAMA PRINCIPAL --------

cliente = Cliente("Maria", "12345678900")
conta = Conta(cliente)

while True:
    print("\n=== MENU ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Valor do depósito: "))
        conta.depositar(valor)

    elif opcao == "2":
        valor = float(input("Valor do saque: "))
        conta.sacar(valor)

    elif opcao == "3":
        conta.mostrar_extrato()

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
