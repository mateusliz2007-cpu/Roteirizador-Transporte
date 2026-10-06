q_clientes = int(input("Quantidade de Clientes: "))
q_rotas = int(input("Quantidade de Rotas: "))

distancia = []
for i in range(q_clientes + 1):  #i = origem 
    linha = []    #todas as distâncias saindo de uma determinada origem
    distancia.append(linha)

    for d in range(q_clientes + 1):  #d = destino
        dist = float(input(f"Qual a Distância do ponto {i} ao {d} "))
        linha.append(dist)

        print(distancia)

distancia_rotas = []
ordens = []

for r in range(q_rotas):

    ordem_cliente = []  #ordem dos clientes visitados

    for q in range (q_clientes):
        cliente_visitado = int(input("Qual Cliente será Visitado Agora: "))
        ordem_cliente.append(cliente_visitado)

        print(ordem_cliente)

    ordens.append(ordem_cliente)
    ponto_atual = 0  #depósito
    soma = 0

    for cliente in ordem_cliente:
        print(ponto_atual, "->", cliente)
        
        dist = distancia[ponto_atual][cliente] #ditância atual até o próximo cliente
        soma += dist
        ponto_atual = cliente

    dist_volta = distancia[ponto_atual][0] #Volta ao depósito
    soma += dist_volta
    distancia_rotas.append(soma)
    print(f"Distância Total da Rota: {soma:.2f}km ")

menor = min(distancia_rotas)
posicao = distancia_rotas.index(menor)  #indexdescobre a posição de determinado valor na lista.
rota = posicao + 1
melhor_ordem = ordens[posicao]

print("0", end=" → ")

for cliente in melhor_ordem:
    print(cliente, end=" → ")
print("0")
