
class Analises:

    def MatrizCorrelacao(df_unificado):
        try:
            # Selecionar apenas as colunas numéricas para análise de correlação
            df_numeric = df_unificado[['Crimes', 'Homicidios', 'Registros', 'Apreendidas', 'IDH', 'Desemprego', 'IPC']]
            
            # Calcular a matriz de correlação
            correlation_matrix = df_numeric.corr()

            # Retornar a matriz de correlação
            return correlation_matrix
        except Exception as e:
            print("Erro ao calcular a matriz de correlação:", e)
            return None

    def AnalisarCorrelacoes(df):
        try:
            # Calcular a matriz de correlação
            matriz_correlacao = df.corr()

            # Verificar se a matriz de correlação foi calculada com sucesso
            if not matriz_correlacao.empty:
                print("Análise das Correlações:")

                # Iterar sobre as linhas da matriz de correlação
                for i, row in matriz_correlacao.iterrows():
                    # Iterar sobre os índices das colunas da matriz de correlação
                    for j in row.index:
                        if i != j:
                            value = matriz_correlacao.loc[i, j]
                            print(f"Correlação entre {i} e {j}: {value:.3f}")

                            # Verificar os limiares e classificar a correlação
                            if abs(value) > 0.8:
                                print(f"Correlação forte entre {i} e {j}")
                            elif abs(value) > 0.5:
                                print(f"Correlação moderada entre {i} e {j}")
                            elif abs(value) > 0.3:
                                print(f"Correlação fraca entre {i} e {j}")
                            else:
                                print(f"Correlação desprezível entre {i} e {j}")

                            print()
            else:
                print("A matriz de correlação está vazia. Verifique se o DataFrame possui dados.")

        except Exception as e:
            print("Ocorreu um erro ao calcular a matriz de correlação:", e)