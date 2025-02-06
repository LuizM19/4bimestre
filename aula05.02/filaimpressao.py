#Vamos simular como funciona o algoritimo de uma impressora que pode receber impressao de diversos comptadores, vamos pensar em uma fila.

class FilaDeImpressao:
    def configurar_inicial(self):
        self.fila=[]
    #isso vai guardar a fila da impressao no vetor

    def adicionar_trabalho(self,trabalho):
        self.fila.append(trabalho)
        print ("Trabalho`{trabalho}` adicionando a fila de impressao")
#remover o trabalho da lista 
    def processar_trabalho(self):
        if not self.fila_vazia():
            trabalho = self.fila.pop(0) #remove o primeiro da fila
            print("Trabalho`{trabalho}` esta processando")
        else:
            print("A fila de impressão está vazia")
#mostrar fila de impressao
    def monstrar_fila(self):
        if self.fila_vazia():
            print("A fila de impressão está vazia")
        else: 
            print("Fila atual de impressao:")
        for trabalho in self.fila:
            print(f"-{trabalho}") #imprimir cada trabalho da lista

    def esta_vazia(self):
        return len(self.fila) == 0


    #funcao de interacao com o usuario
    def menu():
        fila_impressao=FilaDeImpressao()
    #criando uma instancia para a classe 
        fila_impressao.configurar_inicial()
    #configurar os atributos de entrada e saida
        while True:
            print("opção:")
            print("1 - Adicionar um trabalho na fila de impressão")
            print("2 - Imprimir o proximo trabalho da fila")
            print("3 - montrar a fila de impressão")
            print("4 - Sair")
            escolha=input("Digite sua opção:1-4")
            #aqui cai ser lido a escolha do usuario 

            if escolha=="1":
                trabalho = input("Digite o nome do trabalho a ser impresso")
            #maquina da pessoa que esta imprimindo
                fila_impressao.adicionar_trabalho(trabalho)
            elif escolha=="2":
                fila_impressao.processar_trabalho()
            elif escolha=="3":
                fila_impressao.mostrar_fila()
            elif escolha=="4":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")
    menu()  
