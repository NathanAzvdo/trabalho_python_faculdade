# Conjunto imutável de vogais (garante que não será modificado)
VOGAIS = frozenset(['a', 'e', 'i', 'o', 'u'])


def main():
    texto = capturar_texto()
    total_vogais = contar_vogais(texto)
    mostrar_resultado(total_vogais)


def capturar_texto():
    """
    Captura linhas de texto do usuário até que uma linha vazia seja digitada.
    Retorna o texto completo em uma única string.
    """
    linhas = []
    print("Digite seu texto (pressione ENTER em uma linha vazia para encerrar):")
    while True:
        linha = input()
        if not linha:
            break
        linhas.append(linha)
    return "\n".join(linhas)


def contar_vogais(texto):
    """
    Conta o total de vogais no texto e retorna um inteiro.
    """
    return sum(1 for caractere in texto.lower() if caractere in VOGAIS)


def mostrar_resultado(total):
    """
    Exibe o total de vogais encontrado.
    """
    print("\n=== Resultado da Contagem de Vogais ===")
    print(f"TOTAL DE VOGAIS: {total}")


if __name__ == "__main__":
    main()
