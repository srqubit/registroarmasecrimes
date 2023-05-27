from data import Dados
from analises import Analises
from visualizacoes import Visualizacoes

def main():
    try:
        # Definir o ano limite para análise
        limite = 2019

        # Carregar os dados de crimes
        crimes = Dados.Crimes(limite)


        # Carregar os dados de homicídios
        homicidios = Dados.Homicidios(limite)


        # Carregar os dados de registros
        registros = Dados.Registros(limite)


        # Carregar os dados de apreendidas
        apreendidas = Dados.Apreendidas(limite)


        # Carregar os dados de IDH
        idh = Dados.IDH(limite)


        # Carregar os dados de Desemprego
        desemprego = Dados.Desemprego(limite)


        # Carregar os dados de IPC
        ipc = Dados.IPC(limite)


        # Unificar os DataFrames
        df_unificado = Dados.UniData(crimes, homicidios, registros, apreendidas, idh, desemprego, ipc)
        

        # Exportar o DataFrame unificado
        df_unificado.to_csv("graficos/dados/dfUnificado.csv", index=False)


        # Calcular a matriz de correlação
        correlation_matrix = Analises.MatrizCorrelacao(df_unificado)


        #Exportar a matriz de correlação
        correlation_matrix.to_csv("graficos/dados/correlationMatrix.csv", index=False)


        # Analisar as correlações
        Analises.AnalisarCorrelacoes(correlation_matrix)


        # Analisar as variáveis
        Visualizacoes.AnalisarVariaveis(df_unificado)


        # Gerar o mapa de calor
        Visualizacoes.grafico_calor(correlation_matrix)


        # Predição de valores
        df_predicoes = Visualizacoes.predicao(df_unificado)

        # Exportar o DataFrame de predições
        df_predicoes.to_csv("graficos/dados/dfPredicoes.csv", index=False)
        
        # df porcentagem
        df_porcentagem = Visualizacoes.to_percentage(df_predicoes)

        
        Visualizacoes.plot_dataframe(df_porcentagem)
        

        Visualizacoes.grafico_homicidios_registros(df_unificado)

        
    except Exception as e:
        print("Ocorreu um erro durante a execução:", e)


if __name__ == "__main__":
    main()
