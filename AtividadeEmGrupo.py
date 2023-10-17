#importa o csv
import csv
#Cadastra o prouduto 
def cadastra_produto(produtos, nome, valor, quantidade, frete, imposto1, imposto2, imposto3, margem,custo,valor_venda):
    produto = {
        'Nome': nome,
        'Valor': valor,
        'Quantidade': quantidade,
        'Frete': frete,
        'Imposto1': imposto1,
        'Imposto2': imposto2,
        'Imposto3': imposto3,
        'Margem': margem,
        'Custo': custo,
        'Valor_venda': valor_venda  
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")
    print("*************************************")
    print("\n")

# salvar no csv
def salvar_produto(produtos):
    with open('arquivos.csv', mode='w', newline='') as arquivos_csv:
        writer = csv.writer(arquivos_csv)
        writer.writerow(["Nome", "Valos", "Quantidade","Frete","imposto1","imposto2","imposto3","Margem", "Custo", "Valor_venda"])  # Escreve o cabeçalho no arquivo CSV
        for produto in produtos:
            writer.writerow([produto['Nome'], produto['Quantidade'], produto['Frete'], produto['Imposto1'], produto['imposto2'], produto['imposto3'], produto['Margem'],produto['Custo'],produto['Valor_venda']])



def deletar_produto(produto, indice):
    if 0 <= indice < len(produto):
        del produto[indice]
        print("Produto deletado com sucesso!")
    else:
        print("Produto não encontrato, tente novamente.")




while True:
    opc = int(input(f"Bem vindo ao sistema ESTOQUE, escolha uma opção: \n" 
                    "1 - Cadastrar produto: \n" 
                    "2 - Imprimir produtos cadastrados: \n"
                    "3 - Atualizar produto:\n"
                    "4 - Deletar produto:\n"
                    "5 - Saindo do sistema de estoque\n"))

    if opc == 1:

        nome = input("Digite o nome:    ")
        valor = float(input("Digite o valor:    "))
        quantidade = int(input("Digite a quantidade:    "))
        frete = float(input("Digite o frete:    "))
        i1 = float(input("Digite o imposto 1:   "))/100
        i2 = float(input("Digite o imposto 2:   "))/100
        i3 = float(input("Digite o imposto 3:   "))/100
        margem = float(input("Digite a margem:  "))/100

        vlrc=0
        vlrv=0       

        cadastrar_produto(produtos,nome,valor,quantidade,frete,i1,i2,i3,margem,vlrc,vlrv)
    elif opc == 2:
        imprimir_produtos(produtos)
    elif opc == 3:
        indice = int(input("Digite o ID do produto:  "))
        nome = input("Nome do produto:  ")
        valor = float(input("Valor do produto:  "))
        quantidade = float(input("Quantidade do produto:  "))
        frete = float(input("Valor do frete:  "))
        i1 = float(input("Valor do primeiro imposto:  "))
        i2 = float(input("valor do seungo imposto:  "))
        i3 = float(input("Valor do terceiro imposto:  "))
        margem = float(input("Valor da margem desejada:   "))
        vlrc=0
        vlrv=0  

        atualizar_produtos(produtos, indice, nome, valor, quantidade, frete, margem, i1, i2, i3, vlrc, vlrv)
    elif opc == 4:
        indice = int(input("Digite o ID que deseja deletar:"))
        deletar_produto(produtos,indice)
    elif opc == 5:
        print("Escolha uma opção:")
        print("1 - Adicionar;")
        print("2 - Remover;")
        opc = int(input(""))
        indice = int(input("Digite o ID do produto que deseja atualizar:"))
        atualizar_estoque(produtos, indice)
    else:

        break
