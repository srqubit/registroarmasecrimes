from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.signal import argrelextrema
import seaborn as sns
import pandas as pd
import numpy as np


class Visualizacoes:
    def impute_missing(df, column):
        """
        Esta função recebe um dataframe e uma coluna e preenche os valores faltantes na coluna
        com a média dos valores existentes.
        """
        # Verificar se a coluna existe no dataframe
        if column not in df.columns:
            print(f"A coluna {column} não existe no dataframe.")
            return df

        # Verificar se a coluna contém pelo menos um valor não-NaN
        if df[column].isna().all():
            print(f"A coluna {column} contém apenas valores NaN.")
            return df

        try:
            # Calcular a média dos valores existentes
            mean = df[column].mean()

            # Preencher os valores faltantes com a média
            df[column].fillna(mean, inplace=True)

            return df
        except Exception as e:
            print(f"Erro ao preencher os valores faltantes para a coluna {column}:", e)
            return df

    def predicao(df):
        """
        Esta função recebe um dataframe, aplica a função impute_missing para cada coluna do dataframe
        e retorna um dataframe sem valores faltantes.
        """
        try:
            df_filled = df.copy()

            for column in ['Crimes', 'Homicidios', 'Registros', 'Apreendidas', 'IDH', 'Desemprego', 'IPC']:
                df_filled = Visualizacoes.impute_missing(df_filled, column)

            return df_filled
        except Exception as e:
            print("Erro durante a predição de valores faltantes:", e)
            return df

    def to_percentage(df):
        """
        Esta função recebe um dataframe e retorna um dataframe onde os valores de cada coluna foram
        escalonados para o intervalo 0-100 (em porcentagem), sendo que o valor mínimo da coluna é 0%
        e o valor máximo da coluna é 100%.
        """
        try:
            df_percentage = df.copy()

            for column in ['Crimes', 'Homicidios', 'Registros', 'Apreendidas', 'IDH', 'Desemprego', 'IPC']:
                min_val = df[column].min()
                max_val = df[column].max()

                # Se min_val == max_val, todos os valores são iguais. Neste caso, atribuímos 100 a todos os valores.
                if min_val == max_val:
                    df_percentage[column] = 100
                else:
                    df_percentage[column] = (df[column] - min_val) / (max_val - min_val) * 100

            return df_percentage
        except Exception as e:
            print("Erro ao converter valores para porcentagens:", e)
            return df

    def plot_dataframe(df):
        try:
            # Configurar o estilo do Seaborn
            sns.set(style="whitegrid")

            # Ajustar o tamanho da figura para ter uma resolução de 1366x768
            fig = plt.figure(figsize=(19.20, 16.80))

            # Usar gridspec para criar uma grade com duas linhas
            gs = gridspec.GridSpec(2, 1, height_ratios=[4, 1])

            # Desenhar o gráfico de linha na primeira subplot
            ax1 = fig.add_subplot(gs[0])
            colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']  # exemplo de cores
            for idx, column in enumerate(df.columns):
                if column != 'Ano':
                    data = df[column]
                    ax1.plot(df['Ano'], data, label=column, linewidth=2, color=colors[idx % len(colors)])

                    # Encontrar picos e vales
                    diff = data.diff()
                    peaks = (diff.shift(-1) < 0) & (diff > 0)
                    valleys = (diff.shift(-1) > 0) & (diff < 0)

                    ax1.scatter(df['Ano'][peaks], data[peaks], marker='o', color='r')  # marcar picos
                    ax1.scatter(df['Ano'][valleys], data[valleys], marker='o', color='b')  # marcar vales

            ax1.legend()
            ax1.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
            plt.xticks(np.arange(2003, 2020, 1))  # Definir ticks do eixo x de 2003 a 2019

            # Reduzir o número de dígitos decimais na tabela para 2
            table_data = df.round(2).set_index('Ano')

            # Criar a segunda subplot para a tabela
            ax2 = fig.add_subplot(gs[1])
            ax2.axis('off')
            table = ax2.table(cellText=table_data.values,
                            colLabels=table_data.columns,
                            rowLabels=table_data.index,
                            cellLoc='center')

            # Ajustar a posição da tabela para criar um espaço entre as subplots
            table.scale(1, 1.5)  # Ajuste o tamanho vertical da tabela conforme necessário

            # Ajustar a posição da segunda subplot
            ax2.set_position([ax2.get_position().x0, ax2.get_position().y0 + 0.17, ax2.get_position().width, ax2.get_position().height])

            # Salvar o gráfico em um arquivo PNG
            plt.savefig('graficos/grafico_linha.png', dpi=72)

        except Exception as e:
            print("Erro ao plotar o dataframe:", e)

    def AnalisarVariaveis(df):
        try:
            # Extrair as colunas numéricas do DataFrame
            colunas_numericas = df.select_dtypes(include='number').columns

            # Substitui os valores infinitos por NaN e depois remove
            df = df.replace([np.inf, -np.inf], np.nan).dropna()

            # Configurar cores para cada linha
            cores = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

            # Gerar os gráficos de análise para cada variável
            for coluna, cor in zip(colunas_numericas, cores):
                plt.figure(figsize=(10, 8))
                
                # Criar o gráfico com seaborn para um visual mais bonito
                sns.lineplot(data=df, x='Ano', y=coluna, marker='o', lw=2, color=cor)

                # Adicionar anotações com o valor de cada ponto
                for x, y in zip(df['Ano'], df[coluna]):
                    plt.text(x, y, f'{y:.2f}', color=cor, ha='center', va='bottom', fontsize=8, weight='bold')

                # Configurações do gráfico
                plt.title(f'Análise da Variável: {coluna}', fontsize=14, fontweight='bold')
                plt.xlabel('Ano', fontsize=12, fontweight='bold')
                plt.ylabel('Valor', fontsize=12, fontweight='bold')
                plt.grid(True)
                
                # Salvar o gráfico
                plt.savefig(f'graficos/{coluna}.png')
                plt.close()

        except Exception as e:
            print("Ocorreu um erro ao analisar as variáveis:", e)
            

    def grafico_calor(correlation_matrix):
        try:
            # Gerar o mapa de calor
            plt.figure(figsize=(10, 10))
            sns.heatmap(correlation_matrix, annot=True, cmap='Blues')
            plt.title('Mapa de Calor - Correlação entre os dados')
            plt.savefig('graficos/mapa_calor.png', dpi=300)
            plt.close()
        except Exception as e:
            print("Erro ao gerar o mapa de calor:", e)
            return None
    
    def grafico_homicidios_registros(df):
        try:
            # Filtrar o dataframe pelo ano e colunas desejadas
            df = df[(df['Ano'] >= 2003) & (df['Ano'] <= 2019)][['Ano', 'Registros', 'Homicidios']]

            # Exportar os dados para um arquivo CSV
            # df.to_csv('graficos/dados/homicidios_registros.csv', sep=';', index=False)

            fig, ax1 = plt.subplots(figsize=(19.20, 10.80))

            # Plotando o gráfico para 'Registros'
            line1, = ax1.plot(df['Ano'], df['Registros'], marker='o', linewidth=2, label='Registros', color='blue')
            # Adicionando anotações com o valor de cada ponto
            for x, y in zip(df['Ano'], df['Registros']):
                ax1.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color=line1.get_color())

            # Criando um segundo eixo y para 'Homicidios'
            ax2 = ax1.twinx()
            line2, = ax2.plot(df['Ano'], df['Homicidios'], marker='o', linewidth=2, label='Homicidios', color='red')
            # Adicionando anotações com o valor de cada ponto
            for x, y in zip(df['Ano'], df['Homicidios']):
                ax2.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color=line2.get_color())

            # Configurações do gráfico
            ax1.set_xlabel('Ano', fontsize=12, fontweight='bold')
            ax1.set_ylabel('Registros de armas de fogo (CAC)', fontsize=12, fontweight='bold', color='blue')
            ax2.set_ylabel('Homicidios por armas de fogo', fontsize=12, fontweight='bold', color='red')
            ax1.set_title('Tendências ao longo dos anos', fontsize=14, fontweight='bold')
            ax1.legend(loc='upper left', fontsize=12)
            ax2.legend(loc='upper right', fontsize=12)

            # Salvar o gráfico
            plt.savefig('graficos/grafico_homicidios_registros.png')

        except Exception as e:
            print("Erro ao plotar o dataframe:", e)

