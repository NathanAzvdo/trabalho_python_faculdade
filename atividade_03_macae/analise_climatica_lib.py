# analise_climatica_lib.py

import openpyxl
import matplotlib.pyplot as plt

def gerar_arquivo_txt_de_excel(arquivo_excel, nome_planilha, nome_arquivo_saida):
    """
    Lê dados climáticos de uma planilha Excel e os salva em um arquivo de texto (TXT).

    A função extrai os dados de meses e temperaturas (média, mínima e máxima)
    de linhas específicas da planilha e os organiza em um formato de colunas
    separadas por tabulação no arquivo de saída.

    Args:
        arquivo_excel (str): O caminho para o arquivo .xlsx de entrada.
        nome_planilha (str): O nome da aba na planilha que contém os dados.
        nome_arquivo_saida (str): O nome do arquivo .txt a ser gerado.
    """
    workbook = openpyxl.load_workbook(arquivo_excel)
    planilha = workbook[nome_planilha]

    # Extrai os dados das linhas corretas
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

def ler_dados_climaticos_de_txt(caminho_arquivo_txt):
    """
    Lê o arquivo de texto com dados climáticos e retorna listas com os dados.

    Args:
        caminho_arquivo_txt (str): O caminho para o arquivo .txt de entrada.

    Returns:
        tuple: Uma tupla contendo quatro listas: (meses, temperaturas_minima,
               temperaturas_maxima, temperaturas_media).
    """
    meses = []
    temperaturas_minima = []
    temperaturas_maxima = []
    temperaturas_media = []

    with open(caminho_arquivo_txt, mode='r', encoding='utf-8') as arquivo:
        next(arquivo)  # Pula o cabeçalho
        for linha in arquivo:
            partes = linha.strip().split('\t')
            meses.append(partes[0])
            temperaturas_minima.append(float(partes[1]))
            temperaturas_maxima.append(float(partes[2]))
            temperaturas_media.append(float(partes[3]))
            
    return meses, temperaturas_minima, temperaturas_maxima, temperaturas_media

def criar_dicionario_climatico(meses, minimas, maximas, medias):
    """
    Cria um dicionário de dados climáticos a partir de listas.

    Args:
        meses (list): Lista com os nomes dos meses.
        minimas (list): Lista com as temperaturas mínimas.
        maximas (list): Lista com as temperaturas máximas.
        medias (list): Lista com as temperaturas médias.

    Returns:
        dict: Um dicionário contendo os dados climáticos organizados.
    """
    dados_climaticos_dict = {
        "mes": meses,
        "temperatura_minima": minimas,
        "temperatura_maxima": maximas,
        "temperatura_media": medias
    }
    return dados_climaticos_dict

def obter_temp_media_mes(meses, medias, mes_desejado):
    """
    Obtém a temperatura média de um mês específico.

    Args:
        meses (list): Lista com os nomes dos meses.
        medias (list): Lista com as temperaturas médias.
        mes_desejado (str): O nome do mês para o qual a temperatura é desejada.

    Returns:
        float: A temperatura média do mês desejado.
    
    Raises:
        ValueError: Se o mês não for encontrado nos dados.
    """
    try:
        indice = meses.index(mes_desejado)
        return medias[indice]
    except ValueError:
        raise ValueError(f"O mês de '{mes_desejado}' não foi encontrado nos dados.")

def plotar_grafico_temperaturas(meses, minimas, maximas, medias):
    """
    Gera e exibe um gráfico cartesiano das temperaturas mensais.

    Args:
        meses (list): Lista com os nomes dos meses para o eixo X.
        minimas (list): Lista com as temperaturas mínimas para plotagem.
        maximas (list): Lista com as temperaturas máximas para plotagem.
        medias (list): Lista com as temperaturas médias para plotagem.
    """
    plt.figure(figsize=(12, 7))
    plt.plot(meses, minimas, marker='o', linestyle='-', label='Temperatura Mínima (°C)')
    plt.plot(meses, maximas, marker='o', linestyle='-', label='Temperatura Máxima (°C)')
    plt.plot(meses, medias, marker='o', linestyle='--', label='Temperatura Média (°C)')

    plt.title('Variação de Temperatura Mensal em Macaé', fontsize=16)
    plt.xlabel('Mês', fontsize=12)
    plt.ylabel('Temperatura (°C)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()