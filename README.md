# Sistema Bancário V2

Este é um sistema bancário em Python que permite a criação de clientes, contas bancárias e a realização de operações como depósito, saque e exibição de extrato.

**Criado por Jessé Chagas**

👉 [LinkedIn](https://www.linkedin.com/in/jessechagas-dev/)

## Funcionalidades

- Criação de clientes com CPF, nome, data de nascimento e endereço.
- Criação de contas associadas a clientes existentes.
- Depósito de valores em contas.
- Saque de valores de contas, considerando limite diário de saques.
- Exibição de extrato bancário contendo depósitos, saques e saldo atual.
- Listagem de contas e seus titulares.

## Estrutura do Código

O código foi organizado em classes para melhor modularização e organização do sistema.

### Classe Cliente

Representa um cliente do banco e possui os seguintes atributos:

- `cpf`: CPF do cliente.
- `nome`: Nome do cliente.
- `data_nascimento`: Data de nascimento do cliente.
- `endereco`: Endereço do cliente.

### Classe Conta

Representa uma conta bancária e possui os seguintes atributos:

- `agencia`: Número da agência da conta.
- `numero_conta`: Número da conta.
- `titular`: Cliente associado à conta.
- `saldo`: Saldo atual da conta.
- `depositos`: Lista de valores depositados na conta.
- `saques`: Lista de valores sacados da conta.

A classe Conta também possui métodos para depositar, sacar e exibir extrato.

### Classe SistemaBancario

Gerencia a interação com o usuário e possui métodos para criar clientes, criar contas, realizar operações e listar contas.

## Como Executar

Certifique-se de ter o Python instalado em sua máquina.

1. Baixe ou clone este repositório.
2. Abra um terminal na pasta do projeto.
3. Execute o arquivo `sistema_bancario.py` digitando `python sistema_bancario.py`.
