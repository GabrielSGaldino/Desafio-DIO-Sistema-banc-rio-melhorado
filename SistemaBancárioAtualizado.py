
class ContaBancaria:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.transacoes = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 2
        self.limite = 500

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(('Depósito', valor))
        else:
            print("Operação falhou! O valor informado é inválido. Tente novamente!")

    def saque(self, *, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número de saques foi excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.transacoes.append(('Saque', -valor))
            self.numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    def extrato(self, *args, **kwargs):
        print("\n=============EXTRATO==============")
        for transacao, valor in self.transacoes:
            print(f'{transacao}: R$ {valor:.2f}')
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("===============================")

usuarios = []
contas = []

def criar_usuario():
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a data do seu nascimento (dd-mm-aaaa): ")
    cpf = input("Informe o seu CPF (somente número): ")
    endereco = input("Informe o seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuario = {'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco}
    usuarios.append(usuario)
    return usuario

def criar_conta(agencia, numero_conta, usuario):
    conta = ContaBancaria(agencia, numero_conta, usuario)
    contas.append(conta)
    return conta

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[0] Sair
=> """

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        contas[-1].deposito(valor)
    elif opcao == '2':
        valor = float(input("Informe o valor do saque: "))
        contas[-1].saque(valor=valor)
    elif opcao == "3":
        contas[-1].extrato()
    elif opcao == "4":
        criar_usuario()
    elif opcao == "5":
        agencia = "0001"
        numero_conta = len(contas) + 1
        usuario = usuarios[-1]  # Assume o último usuário criado
        criar_conta(agencia, numero_conta, usuario)
    elif opcao =="0":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
