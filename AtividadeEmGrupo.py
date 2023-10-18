#importa o csv
import csv
produtos = []
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

#Deletar o produto
def deletar_produto(produto, indice):
    if 0 <= indice < len(produto):
        del produto[indice]
        print("Produto deletado com sucesso!")
    else:
        print("Produto não encontrato, tente novamente.")

#Deletar o produto dentro do arquivo csv
def deletar_produto_csv(produtos, indice):
    
        with open(produtos.csv, 'r', newline='') as arquivo_csv:
            linhas = list(csv.reader(arquivo_csv))
            
            if 0 <= indice < len(linhas):
                produto_deletado = linhas.pop(indice)
                with open(produtos.csv, 'w', newline='') as arquivo_csv:
                    writer = csv.writer(arquivo_csv)
                    writer.writerows(linhas)
                print(f"Produto deletado com sucesso: {produto_deletado}")
            else:
                print("Produto não encontrado, tente novamente.")

#Função de imprimir
def imprimir_produtos(produtos, produto):
    with open('produto.csv',newline='') as arquivo_csv:

        leitor_csv = csv.reader(arquivo_csv)
        linhas = list(leitor_csv)

    for i,linha in enumerate(linhas):
        if i == 0:
            print(linha)
        Custo = produto['Valor']+(produto['Valor']*produto['Imposto1']+produto['Valor']*produto['Imposto2']+produto['Valor']*produto['Imposto3'])+(produto['Quantidade']/produto['Frete'])
        print(f"{produto['Nome']},{produto['Valor']},{Custo},{produto['Custo']+(Custo*produto['Margem'])},{produto['Quantidade']}")


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
        imposto1 = float(input("Digite o imposto 1:   "))/100
        imposto2 = float(input("Digite o imposto 2:   "))/100
        imposto3 = float(input("Digite o imposto 3:   "))/100
        margem = float(input("Digite a margem:  "))/100

        

        custo=0
        valor_venda=0       

        cadastra_produto(produtos, nome, valor, quantidade, frete, imposto1, imposto2, imposto3, margem,custo,valor_venda)
    elif opc == 2:
        imprimir_produtos(produtos)
    elif opc == 3:
        indice = int(input("Digite o ID do produto:  "))
        nome = input("Nome do produto:  ")
        valor = float(input("Valor do produto:  "))
        quantidade = float(input("Quantidade do produto:  "))
        frete = float(input("Valor do frete:  "))
        imposto1 = float(input("Valor do primeiro imposto:  "))
        imposto2 = float(input("valor do seungo imposto:  "))
        imposto3 = float(input("Valor do terceiro imposto:  "))
        margem = float(input("Valor da margem desejada:   "))
        custo=0
        valor_venda=0  

        atualizar_produtos(produtos, nome, valor, quantidade, frete, imposto1, imposto2, imposto3, margem,custo,valor_venda)
    elif opc == 4:
        indice = int(input("Digite o ID que deseja deletar:"))
        deletar_produto(produtos,indice)
    else:

        break

