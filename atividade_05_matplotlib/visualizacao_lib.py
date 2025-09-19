# matplotlib_visualizacao_lib.py

import matplotlib.pyplot as plt
import numpy as np

def carregar_dados_climaticos_txt(caminho_macae, caminho_rio):
    """
    Carrega os dados climáticos de dois arquivos de texto para arrays NumPy.

    Utiliza a função numpy.loadtxt para carregar as colunas de temperatura,
    ignorando o cabeçalho e a primeira coluna de texto (meses).

    Args:
        caminho_macae (str): O caminho para o arquivo .txt de Macaé.
        caminho_rio (str): O caminho para o arquivo .txt do Rio de Janeiro.

    Returns:
        tuple: Uma tupla contendo dois arrays NumPy (dados_macae, dados_rio),
               cada um com shape (12, 3).
    """
    df_macae = np.loadtxt(caminho_macae, skiprows=1, usecols=[1, 2, 3])
    df_rio = np.loadtxt(caminho_rio, skiprows=1, usecols=[1, 2, 3])
    return df_macae, df_rio

def plotar_grafico_temperaturas_cidade(meses, dados_cidade, nome_cidade):
    """
    Cria e salva um gráfico de linhas 2D das temperaturas de uma cidade.

    Plota as temperaturas mínima, máxima e média ao longo dos meses,
    com estilos de linha e marcadores específicos, e salva a figura em PNG.

    Args:
        meses (numpy.ndarray): Um array com os meses (eixo X).
        dados_cidade (numpy.ndarray): Array (12, 3) com as temperaturas
                                      [min, max, media].
        nome_cidade (str): O nome da cidade, usado no título e no nome do arquivo.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(meses, dados_cidade[:, 0], marker="o", linestyle="-", label="Mínima")
    plt.plot(meses, dados_cidade[:, 1], marker="s", linestyle="-", label="Máxima")
    plt.plot(meses, dados_cidade[:, 2], marker="^", linestyle="None", label="Média")
    plt.title(f"Temperaturas - {nome_cidade}")
    plt.xlabel("Meses")
    plt.ylabel("Temperatura (°C)")
    plt.xticks(meses) # Garante que todos os meses (1-12) sejam mostrados
    plt.legend()
    plt.grid(True)
    
    # Gera nome do arquivo dinamicamente
    nome_arquivo = f"temperaturas_{nome_cidade.lower().replace(' ', '_')}.png"
    plt.savefig(nome_arquivo, dpi=300)
    
    plt.show()

def plotar_comparativo_medias(meses, dados_macae, dados_rio):
    """
    Cria e salva um gráfico de barras agrupadas comparando as temperaturas médias.

    Args:
        meses (numpy.ndarray): Um array com os meses (eixo X).
        dados_macae (numpy.ndarray): Array (12, 3) com os dados de Macaé.
        dados_rio (numpy.ndarray): Array (12, 3) com os dados do Rio de Janeiro.
    """
    media_macae = dados_macae[:, 2]
    media_rio = dados_rio[:, 2]

    largura = 0.35  # Largura das barras
    
    plt.figure(figsize=(10, 6))
    plt.bar(meses - largura/2, media_macae, largura, label="Macaé")
    plt.bar(meses + largura/2, media_rio, largura, label="Rio de Janeiro")

    plt.title("Comparação das Temperaturas Médias")
    plt.xlabel("Meses")
    plt.ylabel("Temperatura Média (°C)")
    plt.xticks(meses)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.savefig("comparacao_medias.png", dpi=300)
    plt.show()