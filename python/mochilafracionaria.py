def calcular_razao(item):
    return item["valor"] / item["peso"]


def mochila_fracionaria(itens, capacidade):

    itens_ordenados = sorted(itens, key=calcular_razao, reverse=True)

    valor_total = 0.0
    capacidade_restante = capacidade
    resultado = []

    for item in itens_ordenados:

        if capacidade_restante == 0:
            break

        quantidade = min(item["peso"], capacidade_restante)

        fracao = quantidade / item["peso"]

        valor_coletado = item["valor"] * fracao

        valor_total += valor_coletado
        capacidade_restante -= quantidade

        resultado.append({
            "nome": item["nome"],
            "razao": calcular_razao(item),
            "peso_original": item["peso"],
            "quantidade_pega": quantidade,
            "fracao": fracao,
            "valor_coletado": valor_coletado,
            "foi_fracionado": fracao < 1.0
        })

    return valor_total, resultado


def coletar_itens():
    itens = []

    print("\n" + "="*50)
    print("  MOCHILA FRACIONÁRIA — Entrada de Dados")
    print("="*50)

    n = int(input("\nQuantos itens você tem? "))

    print(f"\nAgora informe os detalhes de cada um dos {n} itens:\n")

    for i in range(1, n + 1):
        print(f"--- Item {i} ---")
        nome  = input("  Nome:  ")
        peso  = float(input("  Peso (kg): "))
        valor = float(input("  Valor (R$): "))

        if peso <= 0 or valor <= 0:
            print("  [!] Peso e valor devem ser positivos. Item ignorado.")
            continue

        itens.append({"nome": nome, "peso": peso, "valor": valor})
        print()

    capacidade = float(input("Qual é a capacidade da mochila (kg)? "))

    return itens, capacidade


def exibir_resultado(valor_total, resultado, capacidade):
    print("\n" + "="*50)
    print("  RESULTADO")
    print("="*50)

    print("\nItens selecionados (na ordem de escolha do algoritmo):\n")

    for i, r in enumerate(resultado, 1):
        status = "PARCIAL (fracionado)" if r["foi_fracionado"] else "COMPLETO"
        print(f"  {i}. {r['nome']}")
        print(f"     Razão valor/peso : R${r['razao']:.2f}/kg")
        print(f"     Peso disponível  : {r['peso_original']} kg")
        print(f"     Quantidade pega  : {r['quantidade_pega']} kg ({r['fracao']*100:.1f}%) → {status}")
        print(f"     Valor coletado   : R${r['valor_coletado']:.2f}")
        print()

    print(f"  Valor total coletado : R${valor_total:.2f}")

    print("\n" + "="*50)
    print("  RESPOSTAS ÀS QUESTÕES")
    print("="*50)

    print("\n1. Por que o algoritmo escolheu os itens nessa ordem?")
    print("   O algoritmo ordena os itens pela razão valor/peso (R$/kg).")
    print("   Sempre pega primeiro o que dá mais retorno por unidade de peso.")
    print("   Razões (do maior para o menor):")
    for r in resultado:
        print(f"   → {r['nome']}: R${r['razao']:.2f}/kg")

    melhor = max(resultado, key=lambda x: x["razao"])
    print(f"\n2. Maior valor por peso: '{melhor['nome']}' com R${melhor['razao']:.2f}/kg")

    fracionados = [r for r in resultado if r["foi_fracionado"]]
    print("\n3. Itens usados parcialmente:")
    if fracionados:
        for f in fracionados:
            print(f"   → '{f['nome']}': {f['fracao']*100:.1f}% do item ({f['quantidade_pega']} de {f['peso_original']} kg)")
    else:
        print("   Nenhum item foi fracionado — todos couberam inteiros.")

    print("\n4. Complexidade de tempo do algoritmo:")
    print("   → O(n log n) — dominada pela etapa de ordenação.")
    print("     A iteração pelos itens é O(n), mas o sort é O(n log n).")
    print("     No total: O(n log n) + O(n) = O(n log n).")


ITENS_EXEMPLO = [
    {"nome": "Notebook",         "peso": 3.0, "valor": 150.0},
    {"nome": "Câmera fotográfica","peso": 1.5, "valor": 200.0},
    {"nome": "Barraca",          "peso": 5.0, "valor": 80.0},
    {"nome": "Medicamentos",     "peso": 0.5, "valor": 120.0},
    {"nome": "Livros",           "peso": 4.0, "valor": 40.0},
    {"nome": "Comida liofilizada","peso": 2.0, "valor": 100.0},
]

CAPACIDADE_EXEMPLO = 8.0


def main():
    print("\nDeseja usar o conjunto de dados do exemplo? (s/n)")
    escolha = input("> ").strip().lower()

    if escolha == "s":
        itens = ITENS_EXEMPLO
        capacidade = CAPACIDADE_EXEMPLO
        print(f"\nUsando {len(itens)} itens com capacidade de {capacidade} kg.")
    else:
        itens, capacidade = coletar_itens()

    if not itens:
        print("Nenhum item válido fornecido.")
        return

    valor_total, resultado = mochila_fracionaria(itens, capacidade)
    exibir_resultado(valor_total, resultado, capacidade)


if __name__ == "__main__":
    main()
