class Cliente:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class Conta:
    def __init__(self, agencia, numero_conta, titular):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')

    def sacar(self, valor):
        if self.saldo >= valor and valor <= 500 and len(self.saques) < 3:
            self.saldo -= valor
            self.saques.append(valor)
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif valor > 500:
            print('Limite máximo de saque por operação é de R$ 500.00.')
        elif len(self.saques) >= 3:
            print('Limite de 3 saques diários atingido.')
        else:
            print('Saldo insuficiente para saque.')

    def extrato(self):
        print('\nExtrato:')
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações.')
        else:
            for deposito in self.depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in self.saques:
                print(f'Saque: R$ {saque:.2f}')
            print(f'Saldo atual: R$ {self.saldo:.2f}')

class SistemaBancario:
    def __init__(self):
        self.clientes = []
        self.contas = []
        self.agencia = "0001"

    def criar_cliente(self, cpf, nome, data_nascimento, endereco):
        cliente = Cliente(cpf, nome, data_nascimento, endereco)
        self.clientes.append(cliente)
        print("Cliente criado com sucesso.")

    def criar_conta(self, cpf):
        cliente = self.filtrar_cliente(cpf)
        if cliente:
            numero_conta = len(self.contas) + 1
            conta = Conta(self.agencia, numero_conta, cliente)
            self.contas.append(conta)
            print("Conta criada com sucesso.")
        else:
            print("Cliente não encontrado.")

    def filtrar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def listar_contas(self):
        for conta in self.contas:
            print("=" * 100)
            print(f"Agência:\t{conta.agencia}")
            print(f"C/C:\t\t{conta.numero_conta}")
            print(f"Titular:\t{conta.titular.nome}")

    def main(self):
        while True:
            print("\nEscolha uma opção:")
            print("1. Criar cliente")
            print("2. Criar conta")
            print("3. Depositar")
            print("4. Sacar")
            print("5. Extrato")
            print("6. Listar contas")
            print("7. Sair")

            escolha = int(input())

            if escolha == 1:
                cpf = input("Digite o CPF do cliente: ")
                nome = input("Digite o nome do cliente: ")
                data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
                endereco = input("Digite o endereço do cliente: ")
                self.criar_cliente(cpf, nome, data_nascimento, endereco)

            elif escolha == 2:
                cpf = input("Digite o CPF do cliente: ")
                self.criar_conta(cpf)

            elif escolha == 3:
                cpf = input("Digite o CPF do cliente: ")
                valor = float(input("Digite o valor do depósito: "))
                cliente = self.filtrar_cliente(cpf)
                if cliente:
                    conta = None
                    for c in self.contas:
                        if c.titular == cliente:
                            conta = c
                            break
                    if conta:
                        conta.depositar(valor)
                    else:
                        print("Conta não encontrada.")
                else:
                    print("Cliente não encontrado.")

            elif escolha == 4:
                cpf = input("Digite o CPF do cliente: ")
                valor = float(input("Digite o valor do saque: "))
                cliente = self.filtrar_cliente(cpf)
                if cliente:
                    conta = None
                    for c in self.contas:
                        if c.titular == cliente:
                            conta = c
                            break
                    if conta:
                        conta.sacar(valor)
                    else:
                        print("Conta não encontrada.")
                else:
                    print("Cliente não encontrado.")

            elif escolha == 5:
                cpf = input("Digite o CPF do cliente: ")
                cliente = self.filtrar_cliente(cpf)
                if cliente:
                    conta = None
                    for c in self.contas:
                        if c.titular == cliente:
                            conta = c
                            break
                    if conta:
                        conta.extrato()
                    else:
                        print("Conta não encontrada.")
                else:
                    print("Cliente não encontrado.")

            elif escolha == 6:
                self.listar_contas()

            elif escolha == 7:
                break

            else:
                print("Opção inválida. Escolha novamente.")


if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.main()
