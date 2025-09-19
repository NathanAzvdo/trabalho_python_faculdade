# numpy_operacoes_lib.py
import openpyxl
import numpy as np

def gerar_arquivo_txt_com_mes(arquivo_excel, nome_planilha, nome_arquivo_saida):
    """
    Lê dados climáticos (incluindo meses) de uma planilha e os salva em um arquivo TXT.

    Esta função replica a lógica original do notebook: extrai meses e temperaturas
    para listas e depois as escreve em um arquivo de texto de 4 colunas.

    Args:
        arquivo_excel (str): O caminho para o arquivo .xlsx de entrada.
        nome_planilha (str): O nome da aba na planilha que contém os dados.
        nome_arquivo_saida (str): O nome do arquivo .txt a ser gerado.
    """
    workbook = openpyxl.load_workbook(arquivo_excel)
    planilha = workbook[nome_planilha]

    # Extrai os dados para listas, incluindo os meses
    linha_meses = [celula.value for celula in planilha[4][1:]]
    linha_media = [celula.value for celula in planilha[5][1:]]
    linha_minima = [celula.value for celula in planilha[6][1:]]
    linha_maxima = [celula.value for celula in planilha[7][1:]]

    with open(nome_arquivo_saida, mode='w', encoding='utf-8') as arquivo_txt:
        arquivo_txt.write("Mes\tMinima\tMaxima\tMedia\n")
        for i in range(len(linha_meses)):
            mes = linha_meses[i]
            minima = linha_minima[i]
            maxima = linha_maxima[i]
            media = linha_media[i]
            arquivo_txt.write(f"{mes}\t{minima}\t{maxima}\t{media}\n")

def carregar_dados_climaticos_numpy(caminho_arquivo_txt):
    """
    Carrega os dados climáticos de um arquivo de texto para um array NumPy.

    Replica a lógica original do notebook, usando np.loadtxt para carregar
    apenas as colunas numéricas, desempacotá-las e depois transpor o resultado
    para obter o shape (12, 3).

    Args:
        caminho_arquivo_txt (str): O caminho para o arquivo .txt de entrada.

    Returns:
        numpy.ndarray: Um array NumPy com shape (12, 3) contendo as
                       temperaturas [minima, maxima, media].
    """
    array = np.loadtxt(caminho_arquivo_txt, skiprows=1, usecols=(1, 2, 3), unpack=True)
    array_transposed = array.T
    return array_transposed

def analisar_temperatura_media(array_dados):
    """
    Encontra a ocorrência do máximo e mínimo valor na coluna de temperatura média.

    Args:
        array_dados (numpy.ndarray): O array NumPy (12, 3) com os dados climáticos.
                                     Espera-se que a coluna de índice 2 seja a de médias.

    Returns:
        tuple: Uma tupla contendo (maior_media, menor_media).
    """
    coluna_medias = array_dados[:, 2] # A coluna de médias é a de índice 2
    maior_media = np.max(coluna_medias)
    menor_media = np.min(coluna_medias)
    return maior_media, menor_media