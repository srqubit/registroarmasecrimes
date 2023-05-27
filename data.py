import pandas as pd

class Dados:

    def Crimes(limite):
        ''''

            Autor: Ministério da Justiça e Segurança Pública
            Título do site: Dados Nacionais de Segurança Pública - UF
            URL: https://dados.mj.gov.br/dataset/sistema-nacional-de-estatisticas-de-seguranca-publica
            Exemplo de citação no formato ABNT:

            MINISTÉRIO DA JUSTIÇA E SEGURANÇA PÚBLICA. Dados Nacionais de Segurança Pública - UF. Disponível em: https://dados.mj.gov.br/dataset/sistema-nacional-de-estatisticas-de-seguranca-publica. 
            Acesso em: 20 de setembro de 2021.
        '''
        try:
            # Abrir o arquivo .xlsx
            arquivo = 'dados/indicadoressegurancapublicauf.xlsx'
            df = pd.read_excel(arquivo, sheet_name=0)

            # Filtrar o DataFrame para 'Tipo Crime' contendo 'Roubo' ou 'Morte'
            filtro = df['Tipo Crime'].str.contains('Roubo|Morte', case=False)
            df_filtrado = df[filtro]

            # Filtrar os dados até o ano máximo de limite
            df_filtrado = df_filtrado[df_filtrado['Ano'] <= limite]

            # Agrupar e somar a coluna 'Ocorrências' por 'Ano'
            crimes = df_filtrado.groupby('Ano')['Ocorrências'].sum().reset_index()

            # Renomear campo Ocorrências para Crimes
            crimes = crimes.rename(columns={'Ocorrências': 'Crimes'})

            # Retornar o DataFrame crimes
            return crimes
        
        except Exception as e:
            print("Erro ao carregar os dados de crimes:", e)
            return None


    def Homicidios(limite):
        ''''

            Autor: Instituto de Pesquisa Econômica Aplicada (IPEA)
            Título do site: Atlas da Violência
            URL: https://www.ipea.gov.br/atlasviolencia/filtros-series/5/bitos-por-armas-de-fogo
            Exemplo de citação no formato ABNT:

            INSTITUTO DE PESQUISA ECONÔMICA APLICADA (IPEA). Atlas da Violência: Homicídios por Armas de Fogo. Disponível em: https://www.ipea.gov.br/atlasviolencia/filtros-series/5/bitos-por-armas-de-fogo. 
            Acesso em: 20 de setembro de 2021.
        '''
        
        try:
            # Abrir o arquivo .csv com delimitador ponto e vírgula
            arquivo_homicidios = 'dados/homicidios-por-armas-de-fogo.csv'
            df_homicidios = pd.read_csv(arquivo_homicidios, delimiter=';')

            # Selecionar apenas as colunas 'período' e 'valor' e renomear as colunas
            homicidios = df_homicidios[['período', 'valor']].rename(columns={'período': 'Ano', 'valor': 'Ocorrências'})

            # Converter o campo 'Ano' para o tipo inteiro
            homicidios['Ano'] = pd.to_numeric(homicidios['Ano'], errors='coerce')

            # Converter o campo 'Ocorrências' para o tipo inteiro
            homicidios['Ocorrências'] = pd.to_numeric(homicidios['Ocorrências'], errors='coerce')

            # Aplicar filtro com base no ano limite
            homicidios = homicidios[homicidios['Ano'] <= limite]

            # Renomear campo 'Ocorrências' para 'Homicidios'
            homicidios = homicidios.rename(columns={'Ocorrências': 'Homicidios'})

            # Retornar o DataFrame homicidios
            return homicidios
        
        except Exception as e:
            print("Erro ao carregar os dados de homicídios:", e)
            return None


    def IDH(limite):
        ''' 
            Autor: CountryEconomy
            Título do site: CountryEconomy
            URL: https://pt.countryeconomy.com/demografia/idh/brasil
            Título da página: Brasil - Índice de Desenvolvimento Humano
            Exemplo de citação no formato ABNT:

            COUNTRYECONOMY. Brasil - Índice de Desenvolvimento Humano. Disponível em: https://pt.countryeconomy.com/demografia/idh/brasil
            Acesso em: 20 de setembro de 2021.    
        '''
        try:
            # Abrir o arquivo .csv com delimitador ponto e vírgula
            arquivo_idh = 'dados/idh.csv'
            df_idh = pd.read_csv(arquivo_idh, delimiter=';').rename(columns={'Data': 'Ano'}).sort_values('Ano')

            # Converter o campo 'Ano' para o tipo inteiro
            df_idh['Ano'] = df_idh['Ano'].astype(int)

            # Filtrar os dados até o ano máximo de 2019
            idh = df_idh[df_idh['Ano'] <= limite].copy()

            # Converter o campo 'IDH' para o tipo float e substituir a vírgula pelo ponto decimal
            idh['IDH'] = idh['IDH'].str.replace(',', '.').astype(float)

            # Retornar o DataFrame idh
            return idh
        except Exception as e:
            print("Erro ao carregar os dados de IDH:", e)
            return None


    def Desemprego(limite):
        '''       
            Autor: IndexMundi
            Título do site: IndexMundi
            URL: https://www.indexmundi.com/g/g.aspx?c=br&v=74&l=pt
            Título da página: Taxa de desemprego (%)
            Exemplo de citação no formato ABNT:

            INDEXMUNDI. Taxa de desemprego (%). Disponível em: https://www.indexmundi.com/g/g.aspx?c=br&v=74&l=pt. 
            Acesso em: 20 de setembro de 2021.
        '''
        try:
            # Abrir o arquivo .csv com delimitador ponto e vírgula
            arquivo_desemprego = 'dados/desemprego.csv'
            df_desemprego = pd.read_csv(arquivo_desemprego, delimiter=';').sort_values('Ano')

            # Converter o campo 'Ano' para o tipo inteiro
            df_desemprego['Ano'] = df_desemprego['Ano'].astype(int)

            # Converter o campo 'Desemprego' para o tipo float e substituir a vírgula pelo ponto decimal
            df_desemprego['Desemprego'] = df_desemprego['Desemprego'].str.replace(',', '.').astype(float)

            # Aplicar filtro com base no ano limite
            df_desemprego = df_desemprego[df_desemprego['Ano'] <= limite]

            # Retornar o DataFrame df_desemprego
            return df_desemprego
        except Exception as e:
            print("Erro ao carregar os dados de Desemprego:", e)
            return None


    def IPC(limite):
        ''''

            Autor: Transparência Internacional
            Título do site: Transparência Internacional
            URL: https://transparenciainternacional.org.br/ipc/
            Título da página: IPC - Índice de Percepção da Corrupção
            Subtítulo ou descrição: Evolução da nota do Brasil desde 2012
            Exemplo de citação no formato ABNT:

            TRANSPARÊNCIA INTERNACIONAL. IPC - Índice de Percepção da Corrupção: Evolução da nota do Brasil desde 2012. Disponível em: https://transparenciainternacional.org.br/ipc/. 
            Acesso em: 20 de setembro de 2021.

        '''
        try:
            # Abrir o arquivo .csv com delimitador ponto e vírgula
            arquivo_IPC = 'dados/IPC.csv'
            df_IPC = pd.read_csv(arquivo_IPC, delimiter=';').sort_values('Ano')

            # Converter o campo 'Ano' para o tipo inteiro
            df_IPC['Ano'] = df_IPC['Ano'].astype(int)

            # Converter o campo 'IPC' para o tipo inteiro
            df_IPC['IPC'] = df_IPC['IPC'].astype(int)

            # Aplicar filtro com base no ano limite
            df_IPC = df_IPC[df_IPC['Ano'] <= limite]

            # Retornar o DataFrame df_IPC
            return df_IPC
        except Exception as e:
            print("Erro ao carregar os dados do IPC:", e)
            return None


    def Registros(limite):
        # Fonte:
        '''FÓRUM BRASILEIRO DE SEGURANÇA PÚBLICA. 
        Anuário Brasileiro de Segurança Pública, 2022. 
        Brasília, DF: Fórum Brasileiro de Segurança Pública, 2022. 
        p. 282-283. Tabela 60 - 
        Novos Certificados de Registro de Armas de Fogo no SIGMA/Exército Brasileiro, 
        por ano, números absolutos (1), Brasil e Unidades da Federação - 2003-2022.'''

        try:
            # Abrir o arquivo .csv com delimitador ponto e vírgula
            arquivo_registros = 'dados/registro_armas_CR.csv'
            df_registros = pd.read_csv(arquivo_registros, delimiter=';')

            # Filtrar os dados até o ano máximo de limite
            df_registros = df_registros[df_registros['ano'] <= limite]

            # Renomear as colunas 'ano' para 'Ano' e 'registros' para 'Registros'
            registros = df_registros.rename(columns={'ano': 'Ano', 'registros': 'Registros'})

            # Retornar o DataFrame registros
            return registros
        except Exception as e:
            print("Erro ao carregar os dados de registros:", e)
            return None


    def Apreendidas(limite):
        try:
            # Ler o arquivo CSV com separador ponto e vírgula
            df_apreendidas = pd.read_csv('dados/apreendidas.csv', delimiter=';')

            # Filtrar os dados até o ano máximo de limite
            df_apreendidas = df_apreendidas[df_apreendidas['Ano'] <= limite]

            # Totalizar o campo "Qtde Apreensão" pelo campo "Ano"
            df_tot_apreendidas = df_apreendidas.groupby('Ano')['Apreendidas'].sum().reset_index()

            # Ordenar pelo campo "Ano"
            apreendidas = df_tot_apreendidas.sort_values('Ano')

            # Mostrar as informações selecionadas
            return apreendidas
        except Exception as e:
            print("Ocorreu um erro durante a execução:", e)
            return None


    def UniData(crimes, homicidios, registros, apreendidas, idh, df_desemprego, df_IPC):
        try:
            # Converter a coluna 'Ano' para formato numérico em todos os DataFrames
            crimes['Ano'] = pd.to_numeric(crimes['Ano'])
            homicidios['Ano'] = pd.to_numeric(homicidios['Ano'])
            registros['Ano'] = pd.to_numeric(registros['Ano'])
            apreendidas['Ano'] = pd.to_numeric(apreendidas['Ano'])
            idh['Ano'] = pd.to_numeric(idh['Ano'])
            df_desemprego['Ano'] = pd.to_numeric(df_desemprego['Ano'])
            df_IPC['Ano'] = pd.to_numeric(df_IPC['Ano'])

            # Juntar os DataFrames 'crimes', 'homicidios', 'registros', 'apreendidas', 'idh', 'df_desemprego' e 'df_IPC'
            df_merged = crimes.merge(homicidios, on='Ano', how='outer').merge(registros, on='Ano', how='outer').merge(apreendidas, on='Ano', how='outer').merge(idh, on='Ano', how='outer').merge(df_desemprego, on='Ano', how='outer').merge(df_IPC, on='Ano', how='outer')

            # Ordenar pelo campo 'Ano' em ordem crescente
            df_merged = df_merged.sort_values('Ano')

            # Remover os anos anteriores a 2003
            df_merged = df_merged[df_merged['Ano'] >= 2003]

            # Retornar o DataFrame resultante
            return df_merged
        except Exception as e:
            print("Erro ao unificar os DataFrames:", e)
            return None
