import csv
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
    else:

        break
