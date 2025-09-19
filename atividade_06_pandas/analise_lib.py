# pandas_analise_climatica_lib.py

import pandas as pd

def carregar_e_preparar_dados_climaticos(caminho_arquivo_excel):
    """
    Lê os dados climáticos de Macaé e Rio de Janeiro de um arquivo Excel.

    A função carrega as abas especificadas, pula as linhas de cabeçalho,
    seleciona as linhas de dados relevantes, transpõe os DataFrames e
    renomeia as colunas para um formato padronizado.

    Args:
        caminho_arquivo_excel (str): O caminho para o arquivo .xlsx de entrada.

    Returns:
        tuple: Uma tupla contendo os dois DataFrames processados e prontos
               para análise (df_macae, df_rio).
    """
    # Carrega os dados de Macaé
    df_macae = pd.read_excel(
        caminho_arquivo_excel,
        sheet_name="Historico_Clima_Macae",
        skiprows=3,
        index_col=0,
        engine="openpyxl"
    )

    # Carrega os dados do Rio de Janeiro
    df_rio = pd.read_excel(
        caminho_arquivo_excel,
        sheet_name="Historico_Clima_Rio_de_Janeiro",
        skiprows=3,
        index_col=0,
        engine="openpyxl"
    )

    # Seleciona as 6 primeiras linhas de dados e transpõe
    df_macae = df_macae.iloc[:6, :]
    df_rio = df_rio.iloc[:6, :]
    df_macae = df_macae.T
    df_rio = df_rio.T

    # Renomeia as colunas
    colunas = [
        "Media_Temp_C", "Minima_Temp_C", "Maxima_Temp_C",
        "Chuva (mm)", "Umidade(%)", "Dias chuvosos (d)"
    ]
    df_macae.columns = colunas
    df_rio.columns = colunas
    
    return df_macae, df_rio

def calcular_medias_anuais_temperatura(df_macae, df_rio):
    """
    Calcula a média anual das temperaturas para cada cidade.

    Args:
        df_macae (pd.DataFrame): DataFrame com os dados de Macaé.
        df_rio (pd.DataFrame): DataFrame com os dados do Rio de Janeiro.

    Returns:
        tuple: Uma tupla contendo duas Series com as médias de temperatura
               para cada cidade (media_macae, media_rio).
    """
    media_macae = df_macae[["Media_Temp_C", "Minima_Temp_C", "Maxima_Temp_C"]].mean().round(2)
    media_rio = df_rio[["Media_Temp_C", "Minima_Temp_C", "Maxima_Temp_C"]].mean().round(2)
    return media_macae, media_rio

def realizar_analise_detalhada_clima(df_macae, df_rio):
    """
    Executa análises detalhadas para encontrar extremos de temperatura e chuva.

    Args:
        df_macae (pd.DataFrame): DataFrame com os dados de Macaé.
        df_rio (pd.DataFrame): DataFrame com os dados do Rio de Janeiro.

    Returns:
        tuple: Uma tupla contendo dois dicionários com os resultados da análise
               para cada cidade e uma string indicando a cidade mais úmida
               (analise_macae, analise_rio, cidade_mais_umida).
    """
    # Análise para Macaé
    analise_macae = {
        'mes_maior_temp': df_macae["Maxima_Temp_C"].idxmax(),
        'mes_menor_temp': df_macae["Minima_Temp_C"].idxmin(),
        'mes_mais_chuvoso': df_macae["Chuva (mm)"].idxmax(),
        'mes_menos_chuvoso': df_macae["Chuva (mm)"].idxmin(),
        'chuva_anual': df_macae["Chuva (mm)"].sum(),
        'umidade_media': df_macae["Umidade(%)"].mean()
    }
    
    # Análise para o Rio de Janeiro
    analise_rio = {
        'mes_maior_temp': df_rio["Maxima_Temp_C"].idxmax(),
        'mes_menor_temp': df_rio["Minima_Temp_C"].idxmin(),
        'mes_mais_chuvoso': df_rio["Chuva (mm)"].idxmax(),
        'mes_menos_chuvoso': df_rio["Chuva (mm)"].idxmin(),
        'chuva_anual': df_rio["Chuva (mm)"].sum(),
        'umidade_media': df_rio["Umidade(%)"].mean()
    }

    # Comparação de umidade
    cidade_mais_umida = "Macaé" if analise_macae['umidade_media'] > analise_rio['umidade_media'] else "Rio de Janeiro"

    return analise_macae, analise_rio, cidade_mais_umida

def gerar_relatorio_excel(caminho_saida, df_macae, df_rio, medias_macae, medias_rio, analise_macae, analise_rio, cidade_umida):
    """
    Gera um arquivo Excel com o relatório completo da análise climática.

    Args:
        caminho_saida (str): O caminho para o arquivo .xlsx de saída.
        df_macae (pd.DataFrame): O DataFrame original processado de Macaé.
        df_rio (pd.DataFrame): O DataFrame original processado do Rio de Janeiro.
        medias_macae (pd.Series): As médias anuais de temperatura de Macaé.
        medias_rio (pd.Series): As médias anuais de temperatura do Rio de Janeiro.
        analise_macae (dict): Dicionário com os resultados da análise de Macaé.
        analise_rio (dict): Dicionário com os resultados da análise do Rio de Janeiro.
        cidade_umida (str): O nome da cidade mais úmida.
    """
    # Prepara o DataFrame de resumo das análises
    relatorio_analises = pd.DataFrame({
        "Cidade": ["Macaé", "Rio de Janeiro"],
        "Mês maior temp.": [analise_macae['mes_maior_temp'], analise_rio['mes_maior_temp']],
        "Mês menor temp.": [analise_macae['mes_menor_temp'], analise_rio['mes_menor_temp']],
        "Mês mais chuvoso": [analise_macae['mes_mais_chuvoso'], analise_rio['mes_mais_chuvoso']],
        "Mês menos chuvoso": [analise_macae['mes_menos_chuvoso'], analise_rio['mes_menos_chuvoso']],
        "Chuva anual (mm)": [analise_macae['chuva_anual'], analise_rio['chuva_anual']],
        "Umidade média (%)": [analise_macae['umidade_media'], analise_rio['umidade_media']],
        "Cidade mais úmida": [cidade_umida, cidade_umida] # Repete o resultado para ambas as linhas
    })

    # Prepara o DataFrame de médias de temperatura
    relatorio_temperaturas = pd.DataFrame({
        "Cidade": ["Macaé", "Rio de Janeiro"],
        "Média Temp. (°C)": [medias_macae["Media_Temp_C"], medias_rio["Media_Temp_C"]],
        "Mínima Temp. (°C)": [medias_macae["Minima_Temp_C"], medias_rio["Minima_Temp_C"]],
        "Máxima Temp. (°C)": [medias_macae["Maxima_Temp_C"], medias_rio["Maxima_Temp_C"]]
    })

    # Escreve todas as abas no arquivo de saída
    with pd.ExcelWriter(caminho_saida, engine="openpyxl") as writer:
        relatorio_analises.to_excel(writer, sheet_name="Resumo_Analises", index=False)
        relatorio_temperaturas.to_excel(writer, sheet_name="Medias_Temperaturas", index=False)
        df_macae.to_excel(writer, sheet_name="Dados_Macae")
        df_rio.to_excel(writer, sheet_name="Dados_Rio_de_Janeiro")