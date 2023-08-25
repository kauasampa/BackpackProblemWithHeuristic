import time

class Item:
    def __init__(self, nome, peso, valor):
        self.nome = nome
        self.peso = peso
        self.valor = valor

def mochila_gulosa(peso_maximo, itens):
    itens_ordenados = sorted(itens, key=lambda x: x.valor / x.peso, reverse=True)
    peso_total = 0
    valor_total = 0
    itens_selecionados = []

    for item in itens_ordenados:
        if peso_total + item.peso <= peso_maximo:
            itens_selecionados.append(item)
            peso_total += item.peso
            valor_total += item.valor

    return valor_total, itens_selecionados

# MAIN: Recebe os itens que serão cadastrados
'''
itens = []
ans = 's'
while ans.lower() == 's':
    print(f"Adicionando item {len(itens) + 1}:")
    nome = input("Nome: ")
    peso = float(input("Peso (em gramas): "))
    valor = float(input("Valor: "))
    item = Item(nome, peso, valor)
    itens.append(item)
    ans = input("Deseja adicionar outro item? (S/N): ")

peso_maximo = float(input("Peso máximo da mochila: "))'''
itens=[
  Item("MacBook Pro 2023", 1560, 12345.67),
    Item("iPhone 15", 220, 8999.99),
    Item("Samsung 4K Smart TV", 17400, 3499.00),
    Item("Sony Noise-Canceling Headphones", 254, 899.90),
    Item("Nintendo Switch Pro", 398, 2999.50),
    Item("Samsung Galaxy Tab S8", 500, 1499.00),
    Item("Sony PlayStation 5 Pro", 4500, 2599.90),
    Item("Smartwatch Garmin Venu 3", 60, 799.00),
    Item("Câmera Mirrorless Canon EOS M50 Mark II", 387, 1899.99),
    Item("Aspirador Robô Xiaomi Mi Robot Vacuum", 3500, 799.50),
    Item("Monitor Gamer ASUS ROG Swift XG32VQ", 8500, 2399.00),
    Item("Apple AirPods Pro", 45, 549.90),
    Item("Microsoft Surface Laptop 4", 1300, 3499.99),
    Item("GoPro HERO10 Black", 153, 699.00),
    Item("Teclado Mecânico Corsair K95 RGB Platinum", 1250, 799.50),
    Item("GoPro Max 2", 163, 799.00),
    Item("Dell XPS 15 Laptop", 2000, 4299.00),
    Item("Apple Watch Series 7", 47, 899.90),
    Item("Headset Gamer Razer BlackShark V2", 290, 499.00),
    Item("Drone DJI Air 2S", 595, 2499.99),
    Item("Monitor Ultrawide LG 34WL850-W", 6800, 1899.50),
    Item("Amazon Kindle Paperwhite", 182, 499.00),]
peso_maximo = float(10500)  # em gramas

# Chama a função mochila_gulosa
start_time = time.time()  # iniciar cronômetro
valor_maximo, itens_selecionados = mochila_gulosa(peso_maximo, itens)
end_time = time.time()  # parar cronômetro
tempo_decorrido = end_time - start_time  # calcular tempo de execução

# Imprime os resultados
print("Valor máximo possível (abordagem gulosa):", valor_maximo)
print("Itens selecionados:")
for item in itens_selecionados:
    print("Nome:", item.nome, "Peso:", item.peso, "Valor:", item.valor)

print(f'\nTempo decorrido: {tempo_decorrido} segundos')

