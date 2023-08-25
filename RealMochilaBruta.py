import time

def mochilaForcaBruta(pesos, capacidade, valores):
    NumeroDeItens = len(valores)
    melhor_valor = 0
    melhor_combinacao = []

    # Gera todas as combinações possíveis
    for i in range(2 ** NumeroDeItens):
        combinacao = []
        peso_total = 0
        valor_total = 0

        # Verifica cada bit para decidir se o item é selecionado ou não
        for j in range(NumeroDeItens):
            if (i >> j) & 1:
                combinacao.append(j)
                peso_total += pesos[j]
                valor_total += valores[j]

        # Verifica se a combinação atual é válida e se tem um valor maior
        if peso_total <= capacidade and valor_total > melhor_valor:
            melhor_valor = valor_total
            melhor_combinacao = combinacao

    return melhor_valor, melhor_combinacao

def MainMenu():
    nomes=[]
    valores=[]
    pesos=[]
    while(True):
        option=int(input('Escolha a opção desejada:\n1-Adicionar eletrônico\n2-Listar Itens\n3-Ditar Capacidade total\n4-Prosseguir\n'))
        if option==1:
            nome=input('Digite o nome do eletrônico:')
            peso=float(input('Digite o peso do eletrônico em kg:'))
            valor=float(input('Digite o valor do eletrônico:'))
            nomes.append(nome)
            pesos.append(peso)
            valores.append(valor)

        elif option==2:
            for nomeX,pesoX,valorX in zip(nomes,pesos,valores):
                print(f'Nome do eletrônico:{nomeX}\nPeso do eletrônico:{pesoX}Kg\nValor do eletrônico:R${valorX}')
                print('\n')
        elif option==3:
            capacidade=float(input('Digite a capacidade da mochila em kg:'))
        elif option==4:
            break
        else:
            print('Opção inválida, digite novamente:\n')

    return capacidade, pesos, valores,nomes

PesosFinais=[]
ValoresFinais=[]
NomesFinais=[]
capacidadeFinal, PesosFinais, ValoresFinais,NomesFinais=MainMenu()

CombinacaoFinal=[]
start_time=time.time()#iniciar cronômetro
ValorMaximo, CombinacaoFinal=mochilaForcaBruta(PesosFinais, capacidadeFinal, ValoresFinais)
end_time=time.time()#parar cronômetro
tempo_decorrido = end_time - start_time#calcular tempo de execução


print(f'Valor máximo da combinação:{ValorMaximo}\n')
i=0
for p in CombinacaoFinal:
     print(f'Item {i+1}: {NomesFinais[p]}\n')
     i+=1

print(f'\nTempo decorrido: {tempo_decorrido} segundos')