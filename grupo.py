from datetime import datetime   #Chama de biblioteca
import csv #Chamada de biblioteca
# cadastrar


tarefas = [] #Definindo o Array


# CRIAR TAREFA

def criar_tarefa(tarefas):
    tarefa = {
        'Nome': input("Digite o nome da tarefa: "),
        'Tipo': input("Insira o tipo de tarefa: "),
        'Observacao': input("Informe a observação da tarefa:"),
        'Data de entrega': input("Insira a data da tarefa: AAAA-MM-DD "),
    }

    tarefas.append(tarefa)
    criar_csv()
    print("")
    print("Tarefa cadastrada com sucesso!")
    print("")


#CRIAR CSV

def criar_csv():
    gravador = csv.writer(open('arquivo_tarefa.csv', mode="w", newline='')) 
    gravador.writerow(["Nome","Tipo","Observacao","Data de entrega"])

    for tarefa in tarefas:
            nome = tarefa['Nome']
            tipo = tarefa['Tipo']
            observacao = tarefa['Observacao']
            data_de_entrega = tarefa['Data de entrega']
            gravador.writerow([tarefa['Nome'],tarefa['Tipo'],tarefa['Observacao'],tarefa['Data de entrega']])


#IMPRIMIR


def ler_e_imprimir_csv(tarefas):

    with open('arquivo_tarefa.csv', 'r', newline='') as arquivo_tarefa:
        linhas = csv.reader(arquivo_tarefa)
        for linha in linhas:
            print(linha[0],linha[1],linha[2],linha[3])  

#ATUALIZAR


def atualizar_tarefa(tarefas):
    nome_tarefa = input("Digite o nome da tarefa que deseja atualizar: ")
    
    tarefa_encontrada = None
    for tarefa in tarefas:
        if tarefa['Nome'] == nome_tarefa:
            tarefa_encontrada = tarefa
            break

    if tarefa_encontrada:
        # Exibir os detalhes da tarefa
        print("\nDetalhes da tarefa a ser atualizada:")
        print("Nome:", tarefa_encontrada['Nome'])
        print("Tipo:", tarefa_encontrada['Tipo'])
        print("Observacao:", tarefa_encontrada['Observacao'])
        print("Data de entrega:", tarefa_encontrada['Data de entrega'])

        # Solicitar as novas informações da tarefa
        tarefa_atualizada = {
            'Nome': input("Digite o novo nome da tarefa: "),
            'Tipo': input("Insira o novo tipo de tarefa: "),
            'Observacao': input("Informe a nova observação da tarefa:"),
            'Data de entrega': input("Insira a nova data da tarefa (AAAA-MM-DD): "),
        }

        # Atualizar a tarefa na lista
        tarefa_encontrada.update(tarefa_atualizada)
        criar_csv()
        print("\nTarefa atualizada com sucesso!\n")
    else:
        print("\nTarefa nao encontrada!\n")


# imprimir tarefas (concluidas,em atraso) em csv
# editar tarefa
# deletar

while True:
    print("-------  AGENDA  ------")
    print("1. Cadastrar tarefa.")
    print("2. imprimir todas as tarefas")
    print('3. Imprimir tarefas em aberto.')
    print("5. Atualizar Tarefas")
    print("4. Editar tarefas.")
    print("6. Sair.")
    print("\n")
    op = int(input("escolha uma opção:"))
    if op == 1:
        criar_tarefa(tarefas)
    elif op == 2:
        ler_e_imprimir_csv(tarefas)
    elif  op == 3:
        print("\n")
    elif op == 4: 
        print("\n")
    elif op == 5:
        atualizar_tarefa(tarefas)
    elif op == 6:
        break
    else: 
        print("-------------------")
        print("  OPÇÃO INVALIDA   ")
        print('-------------------')
