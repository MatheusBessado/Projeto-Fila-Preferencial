class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class FilaDeEspera:
    def __init__(self):
        self.head = None
        self.contadorV = 1
        self.contadorA = 201

    def inserirFilaComPrioridade(self, novo_nodo):
        if self.head is None or self.head.cor == 'V':
            novo_nodo.proximo = self.head
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            novo_nodo.proximo = atual.proximo
            atual.proximo = novo_nodo

    def inserirFilaSemPrioridade(self, novo_nodo):
        if self.head is None:
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def inserirCor(self):
        cor = input('Digite a letra do seu cartão: V (Sem Prioridade) ou A (Com Prioridade): ').upper()

        if cor == 'V':
            numero = self.contadorV
            self.contadorV += 1
        elif cor == 'A':
            numero = self.contadorA
            self.contadorA += 1
        else:
            print("Cor inválida. Use apenas 'A' ou 'V'.")
            return

        novo_nodo = Nodo(numero=numero, cor=cor)

        if cor == 'A':
            self.inserirFilaComPrioridade(novo_nodo)
        else:
            self.inserirFilaSemPrioridade(novo_nodo)

    def imprimirFilaDeEspera(self):
        atual = self.head
        print("\nFila de Espera:")
        if not atual:
            print("Fila vazia.")
        while atual:
            print(f"Cartão {atual.numero} - Cor {atual.cor}")
            atual = atual.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Nenhum paciente na fila.")
        else:
            print(f"Atendendo Paciente Cartão {self.head.numero} - Cor {self.head.cor}")
            self.head = self.head.proximo

    def menu(self):
        while True:
            print("\nMenu:")
            print("1 - Adicionar Paciente à Fila")
            print("2 - Mostrar Fila de Pacientes")
            print("3 - Chamar Paciente")
            print("4 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.inserirCor()
            elif opcao == "2":
                self.imprimirFilaDeEspera()
            elif opcao == "3":
                self.atenderPaciente()
            elif opcao == "4":
                print("Encerrando sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Execução do sistema
fila = FilaDeEspera()
fila.menu()

