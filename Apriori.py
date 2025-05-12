from itertools import combinations
import preprocessamento


def get_frequent_items(transactions, min_support):
    """Encontra conjuntos frequentes com base no suporte mínimo."""
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1

    return {item for item, count in item_counts.items() if count >= min_support}
def generate_combinations(items, size):
    """Gera combinações possíveis dos itens."""
    return [set(comb) for comb in combinations(items, size)]
def calculate_support(transactions, item_sets):
    """Calcula o suporte de cada conjunto de itens."""

    support_counts = {frozenset(item_set): 0 for item_set in item_sets}
    for transaction in transactions:
        for item_set in item_sets:
            if item_set.issubset(transaction):
                support_counts[frozenset(item_set)] += 1

    return support_counts

min_support = 5
frequent_items    = get_frequent_items(preprocessamento.cesta_usuarios, min_support)
item_combinations = generate_combinations(frequent_items, 2)
support_counts    = calculate_support(preprocessamento.cesta_usuarios, item_combinations)
print("Filmes Frequentes:", frequent_items)
print("\nSuporte dos Conjuntos de 2 Filmes:")
for item_set, support in support_counts.items():
    if support > 0:  # Imprime apenas conjuntos com suporte maior que zero
        print(f"Conjunto: {tuple(item_set)}, Suporte: {support}")
