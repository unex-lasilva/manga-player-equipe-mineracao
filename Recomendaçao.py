import preprocessamento
from Apriori import calculate_support, generate_combinations, get_frequent_items

# Parâmetros
min_support = 5
transacoes = preprocessamento.cesta_usuarios

# Itens frequentes
frequent_items = get_frequent_items(transacoes, min_support)

# Combinações de tamanho 1 e 2
combinacoes_1 = generate_combinations(frequent_items, 1)
combinacoes_2 = generate_combinations(frequent_items, 2)

# Suportes de tamanho 1 e 2
suportes_1 = calculate_support(transacoes, combinacoes_1)
suportes_2 = calculate_support(transacoes, combinacoes_2)

# Unir tudo
suportes = {**suportes_1, **suportes_2}

# Função de regras com suporte correto
def gerar_regras_associacao(suportes, min_conf=0.5):
    regras = []

    for itemset in suportes:
        if len(itemset) == 2:
            itemset = list(itemset)
            a, b = itemset[0], itemset[1]

            suporte_ab = suportes[frozenset([a, b])]
            suporte_a  = suportes.get(frozenset([a]), 1)
            suporte_b  = suportes.get(frozenset([b]), 1)

            confianca_a_para_b = suporte_ab / suporte_a
            confianca_b_para_a = suporte_ab / suporte_b

            if confianca_a_para_b >= min_conf:
                regras.append((a, b, confianca_a_para_b))
            if confianca_b_para_a >= min_conf:
                regras.append((b, a, confianca_b_para_a))

    return regras

# Gerar regras com confiança mínima de 0.5
regras = gerar_regras_associacao(suportes, min_conf=0.5)

# Exibir regras
print("\nRegras de Recomendação:")
for antecedente, consequente, confianca in regras:
    print(f"Se gostou de '{antecedente}', então pode gostar de '{consequente}' (Confiança: {confianca:.2f})")
