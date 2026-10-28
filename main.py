def apresentar_menu():
    print("\n" + "=" * 32)
    print("       LISTA DE COMPRAS")
    print("=" * 32)
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar quantidade/preço")
    print("4 - Remover produto")
    print("5 - Calcular total da lista")
    print("0 - Sair")
    print("=" * 32)


def adicionar_produto(lista_compras):
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Aviso: O nome do produto não pode ficar vazio.")
        return

    for item in lista_compras:
        if item["nome"].lower() == nome.lower():
            print(f"O produto '{nome}' já existe. Utilize a opção de atualização.")
            return

    try:
        quantidade = int(input(f"Quantidade de '{nome}': "))
        preco = float(input(f"Preço unitário de '{nome}': "))
        if quantidade <= 0 or preco < 0:
            print("Erro: A quantidade deve ser positiva e o preço não pode ser negativo.")
            return
    except ValueError:
        print("Erro: Insira valores numéricos válidos.")
        return

    item = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    lista_compras.append(item)
    print(f"Produto '{nome}' adicionado com sucesso!")


def listar_produtos(lista_compras):
    if not lista_compras:
        print("A lista de compras está vazia.")
        return

    print(f"\n{'Nº':<4} {'Produto':<20} {'Qtd':<8} {'Preço Unit.':<14} {'Subtotal':<10}")
    print("-" * 60)
    for i, item in enumerate(lista_compras, start=1):
        subtotal = item["quantidade"] * item["preco"]
        print(f"{i:<4} {item['nome']:<20} {item['quantidade']:<8} {item['preco']:<14.2f} {subtotal:<10.2f}")


def atualizar_produto(lista_compras):
    listar_produtos(lista_compras)
    if not lista_compras:
        return

    nome = input("\nNome do produto a atualizar: ").strip()
    for item in lista_compras:
        if item["nome"].lower() == nome.lower():
            try:
                nova_qtd = int(input(f"Nova quantidade para '{item['nome']}': "))
                novo_preco = float(input(f"Novo preço para '{item['nome']}': "))
                if nova_qtd <= 0 or novo_preco < 0:
                    print("Valores inválidos.")
                    return
                item["quantidade"] = nova_qtd
                item["preco"] = novo_preco
                print(f"Item '{item['nome']}' atualizado com sucesso!")
                return
            except ValueError:
                print("Erro: Entrada numérica inválida.")
                return

    print(f"Produto '{nome}' não encontrado.")


def remover_produto(lista_compras):
    listar_produtos(lista_compras)
    if not lista_compras:
        return

    nome = input("\nNome do produto a remover: ").strip()
    for i, item in enumerate(lista_compras):
        if item["nome"].lower() == nome.lower():
            del lista_compras[i]
            print(f"Produto '{nome}' removido com sucesso!")
            return

    print(f"Produto '{nome}' não encontrado.")


def calcular_total(lista_compras):
    if not lista_compras:
        print("A lista está vazia. Total: 0.00")
        return

    total = sum(item["quantidade"] * item["preco"] for item in lista_compras)
    print(f"\nValor total acumulado: {total:.2f}")


def executar_sistema():
    compras = []

    while True:
        apresentar_menu()
        opcao = input("Selecione uma opção: ").strip()

        if opcao == "1":
            adicionar_produto(compras)
        elif opcao == "2":
            listar_produtos(compras)
        elif opcao == "3":
            atualizar_produto(compras)
        elif opcao == "4":
            remover_produto(compras)
        elif opcao == "5":
            calcular_total(compras)
        elif opcao == "0":
            print("\nA encerrar o sistema. Até breve!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    executar_sistema()
