def main():
    numeros = realizar_inputs()
    exibir_resultados(numeros)


def realizar_inputs():
    """Solicita ao usuário a quantidade de números e os lê como float."""
    n = int(input("Quantos números você deseja digitar? "))
    return [float(input(f"Digite o {i+1}º número: ")) for i in range(n)]


def retorna_valores_pares(numeros):
    """Retorna os valores que estão em índices pares."""
    return [numeros[i] for i in range(len(numeros)) if i % 2 == 0]


def retorna_valores_impares(numeros):
    """Retorna os valores que estão em índices ímpares."""
    return [numeros[i] for i in range(len(numeros)) if i % 2 != 0]


def arredondar_valores(numeros, casas):
    """Arredonda os valores para a quantidade de casas decimais especificada."""
    return [round(num, casas) for num in numeros]


def somatorio_valores(numeros):
    """Retorna o somatório dos valores com 2 casas decimais."""
    return round(sum(numeros), 2)


def arredondar_para_inteiro(numeros):
    """Arredonda os valores para o inteiro mais próximo."""
    return [round(num) for num in numeros]


def converter_binario(numeros_int):
    """Converte valores inteiros para binário."""
    return [bin(num) for num in numeros_int]


def converter_octal(numeros_int):
    """Converte valores inteiros para octal."""
    return [oct(num) for num in numeros_int]


def converter_hexadecimal(numeros_int):
    """Converte valores inteiros para hexadecimal."""
    return [hex(num) for num in numeros_int]


def exibir_resultados(numeros):
    """Centraliza toda a exibição dos resultados."""
    numeros_int = arredondar_para_inteiro(numeros)

    print("\nNúmeros nas posições pares:", retorna_valores_pares(numeros))
    print("Números nas posições ímpares:", retorna_valores_impares(numeros))

    print("\nNúmeros arredondados com 1 casa decimal:", arredondar_valores(numeros, 1))
    print("Números arredondados com 2 casas decimais:", arredondar_valores(numeros, 2))

    print("\nSomatório dos números (arredondado para 2 casas decimais):", somatorio_valores(numeros))

    print("\nNúmeros arredondados para o inteiro mais próximo:", numeros_int)
    print("Números convertidos para binário:", converter_binario(numeros_int))
    print("Números convertidos para octal:", converter_octal(numeros_int))
    print("Números convertidos para hexadecimal:", converter_hexadecimal(numeros_int))


if __name__ == "__main__":
    main()
