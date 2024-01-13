import re
import pandas as pd


def questionamentos(celula):
    print("Função questionamentos: Em andamento")
    # Abrindo a planilha de Judicialização para usar as listas padronizadas
    nome_arq = 'Judicializacao.xlsx'
    planilha_judi = pd.read_excel(nome_arq, sheet_name='Listas')

    # Arrumando a tipologia do dado de float para string
    planilha_judi['tipo_processo'] = planilha_judi['tipo_processo'].astype(str)
    planilha_judi['Prestadora'] = planilha_judi['Prestadora'].astype(str)
    motivo = planilha_judi['tipo_processo'].iloc[25:61].values
    teses = planilha_judi['Prestadora'].iloc[25:182].values

    # Padronização e limpeza de dados desnecessários para a análise
    motivo_limpo = [m.lower().replace('/ ', '/') for m in motivo]
    tese_limpa = [t.lower().replace('\u202f', ' ').replace('\xa0', '')
                  for t in teses]
    questionamentos = celula.text.lower().replace('/ ', '/').replace('\xa0', ' ').split('\n\n')

    # Lista dos questionamentos encontrados no processo
    titulo_questionamento = []

    # Lista apenas dos questionamentos encontrados no processo, sem a indexação
    titulo_questionamento_limpo = []

    # Lista dos index dos questionamentos baseado no padrão da planilha de Judicalização
    index_questionamento = []

    # Lista dos títulos de questionamentos junto com o index padrão da planilha de Judicialização
    questionamento_padronizado = []

    # Lista das teses de cada questionamento encontradas no processo
    tese_questionamento = []

    # Lista dos index das teses de cada questionamento, baseada no padrão da planilha de Judicialização
    index_tese = []

    # Lista das teses dos questionamentos junto com o index padrão da planilha de Judicialização
    tese_padronizada = []

    # Loop para extrair o título do questionamento e suas respectivas teses e salvar em duas listas diferentes, o número de títulos e teses é igual
    print("Função questionamentos - Extraindo títulos e teses: Em andamento")
    for ocorrencia in questionamentos:
        # Coloca cada título de questionamento e a tese em uma lista
        linhas = ocorrencia.strip().split('\n')
        # Pega a primeira string de linhas, que são os títulos dos questionamentos
        titulo = linhas[0].strip()
        # linhas[1:] para que use apenas as teses,ignorandos os títulos
        for descricao in linhas[1:]:
            descricao_formatada = descricao.strip()
            if descricao_formatada:
                # Para cada tese é atribuído um título, baseando-se na listas "linhas" que contém títulos com mais de uma tese
                titulo_questionamento.append(titulo)
                tese_questionamento.append(descricao)
    print("Função questionamentos - Extraindo títulos e teses: Finalizada")

    print("Função questionamentos - Indexação do título: Em andamento")
    for i in titulo_questionamento:
        # Regex para dividir a indexação do título do questionamento em dois grupos
        # resultado_motivo = re.search(r'^\d+(\.\d+)*\.\s+(.*)', i)
        resultado_motivo = re.search(
            r'^\d{2}\.\d{1,2}(\.\s+|\.\s+|\s+|\s+)(.*)', i)
        if resultado_motivo:
            # Usando o group(2) para ignorar a indexação e salvar apenas o título do questionamento
            conteudo_motivo = resultado_motivo.group(2)
            titulo_questionamento_limpo.append(conteudo_motivo)
    print("Função questionamentos - Indexação do título: Finalizada")

    # Padronização e limpeza de dados desnecessários para a análise
    tese_quest = [auxiliar.strip() for auxiliar in tese_questionamento]
    tese_questionamento = [
        t.lstrip('-').strip() if t.startswith('-') else t.strip() for t in tese_quest]

    # Loop para encontrar qual o index padrão, baseado na planilha de Judicialização, dos questionamentos do processo
    print("Função questionamentos - Indexação do questionamento: Em andamento")
    for elemento in titulo_questionamento_limpo:
        for string in motivo_limpo:
            if elemento in string:
                index_questionamento.append(string[:2])
    print("Função questionamentos - Indexação do questionamento: Finalizada")

    # Loop para encontrar qual o index padrão, baseado na planilha de Judicialização, das teses de cada questionamento do processo
    print("Função questionamentos - Indexação da tese: Em andamento")
    for item in tese_questionamento:
        flag = False
        for p in tese_limpa:
            if item in p:
                flag = True
                # Regex para dividir a indexação da tese de cada questionamento em dois grupos
                result = re.search(r'\b(\d{2}\.\d{1,2})\b', p)
                if result:
                    # Usando o group(1) para ignorar a tese e salvar apenas a indexação
                    index_tese.append(result.group(1))
        if not flag:
            index_tese.append("0")
    print("Função questionamentos - Indexação da tese: Finalizada")

    print("Função questionamentos - Padrão de questionamento: Em andamento")
    # Loop para procurar o index dos questionamentos na planilha de Judicialização e salva-los no padrão
    for num in index_questionamento:
        for frase in motivo:
            if num in frase:
                questionamento_padronizado.append(frase)
    print("Função questionamentos - Padrão de questionamento: Finalizada")

    # Loop para procurar o index das teses dos questionamentos na planilha de Judicialização e salva-los no padrão
    print("Função questionamentos - Padrão de tese: Em andamento")
    for cod in index_tese:
        flag = False
        # Regex para pegar a exata correspondência do index da tese
        regex = r'\b(' + re.escape(cod) + r')\b'
        for t in teses:
            # Se o index salvo na lista index_tese for exatamente igual a algum da lista padrão teses toda a string é salva
            if re.search(regex, t):
                flag = True
                tese_padronizada.append(t)
        if not flag:
            tese_padronizada.append("Sem acesso à informação")
    print("Função questionamentos - Padrão de tese: Em andamento")

    # Excluindo informações que sobraram caso precise
    if len(tese_padronizada) > len(questionamento_padronizado):
        del tese_padronizada[len(questionamento_padronizado)]

    print("Função questionamentos: Finalizada")
    return titulo_questionamento_limpo, questionamento_padronizado, tese_padronizada
