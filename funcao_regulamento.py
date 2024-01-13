import re

def regulamento(celula):
    #Colocando cada regulamento em uma linha
    print("Função regulamento: Em andamento")
    regulamento_teste = celula.text.replace('\t',' ').split('\n\n')
    regulamento = [item for item in regulamento_teste if item.strip() != '']
    
    descricao = []
    regulamento_dispositivo = []
    norma = []
    dispositivo = []
    indices_reg = []
    indices_disp = []
    lista_dispositivos = []
    lista_regulamentos = []
    lista_unica = []

    #Divisão para que regulamentos que dividem a mesma descrição fiquem em linhas separadas
    regulamento = [r.split('c/c') for r in regulamento]

    print("Função regulamento - Criando sublistas: Em andamento")
    for sublista in regulamento:
        if len(sublista) > 1:
            #A descrição dos regulamentos aparece no último elemento, então a divisão precisa ser feita nele
            #Então, a string fica divida em dois, o que vem antes do : e o que vem depois
            partes_segunda_string = sublista[-1].split(':', 1)
            if len(partes_segunda_string) > 1:
                descricao_unica = partes_segunda_string[1].strip()
                #Concatena a descrição que foi retirada da última string para que fique nas outras também
                for c in range(len(sublista)-1):
                    sublista[c] += ': ' + descricao_unica
    print("Função regulamento - Criando sublistas: Finalizada")

    #Loop aninhado para retirar os elementos das sublistas e transformar tudo em uma única lista
    lista_unica = [item.strip() for sublist in regulamento for item in sublist]
    
    #Criando um regex para pegar o que vem depois do : e um para o que vem antes
    print("Função regulamento - Dividindo o que vem antes e depois de ':' : Em andamento")
    for desc in lista_unica:
        posterior = re.search (r'[^:]*:(.*)', desc)
        anterior = re.search(r'(.*?):', desc)
        #O que vem depois do : é salvo como descricao
        if posterior:
            conteudo_post = posterior.group(1)
            descricao.append(conteudo_post.strip())
        #O que vem antes do : é salvo como regulamento e dispositivo
        if anterior:
            conteudo_ant = anterior.group(1)
            regulamento_dispositivo.append(conteudo_ant)
    print("Função regulamento - Dividindo o que vem antes e depois do ':' : Finalizada")
    regulamento_min = [rd.lower() for rd in regulamento_dispositivo]
    
    #Padrão de regulamentos de acordo com a planilha de Judicializacao
    padrao_regulamento =  [r'\bato\b',
                           r'\bcontrato\b',
                           r'dec\.',
                           r'\bdespacho\b',
                           r'\blei\b',
                           r'\bnorma\b',
                           r'\bres\b',
                           r'\btermo\b',
                           r'\btermos\b',
                           r'\bdecreto\b'
                          ]

    #Padrão de dispositivos de acordo com a planilha de Judicializacao
    padrao_dispositivo = [r'\banexo\b',
                          r'art\.',
                          r'\bcláusula\b',
                          r'\bcláusulas\b',
                          r'\bdespacho cautelar\b',
                         ]
    #Padrão para 'item' pois ele pode vir como dispositivo ou como complemento de algum dispositivo
    #O padrao_final só será usado se antes dele não tiver nenhum dos outros dispositivos, ou seja, ele é um dispositivo e não um complemento
    padrao_final = r'^item\b'
    #Loop para encontrar o indice inicial e final em que algum padrao de regulamento é encontrado
    print("Função regulamento - Busca pelo padrao de regulamento : Em andamento")
    for rm in regulamento_min:
        for pr in padrao_regulamento:
            matches = re.finditer(pr, rm)
            for match in matches:
                norma.append(match)
    
    #Loop para que se consiga ler o indice do regex
    for match in norma:
        span = match.span()
        indices_reg.append(span)
    print("Função regulamento - Busca pelo padrao de regulamento : Finalizada")
    
    #Loop para encontrar o indice inicial e final em que algum padrao de dispositivo é encontrado
    print("Função regulamento - Busca pelo padrao de dispositivo : Em andamento")
    for aux_rm in regulamento_min:
        #Caso algum regex do padrao_dispositivo seja encontrado ele é salvo na lista dispositivo
        for pd in padrao_dispositivo:
            ocorrencias = re.finditer(pd, aux_rm)
            for ocorrencia in ocorrencias:
                dispositivo.append(ocorrencia)
        #Exceção para quando o dispositivo possui a palavra item
        #Caso o regex de item(padrao_final) seja encontrado ele é salvo, também, na lista dispositivo
        ocorrencias_final = re.finditer(padrao_final, aux_rm)
        for ocorrencia_final in ocorrencias_final:
            dispositivo.append(ocorrencia_final)
    
    #Loop para que se consiga ler o indice do regex
    for ocorrencia in dispositivo:
        index = ocorrencia.span()
        indices_disp.append(index)
    print("Função regulamento - Busca pelo padrao de dispositivo : Finalizada")
    
    #Excluir informações que ficaram sobrando
    del lista_unica[len(indices_disp):]
    
    print("Função regulamento - Encontrando o que é regulamento e o que é dispositivo : Em andamento")
    for i, string in enumerate(lista_unica):
        #Variável com o indice em que o dispositivo foi encontrado
        inicio_disp = indices_disp[i][0]
        #Variável com o indice em que o regulamento foi encontrado
        inicio_reg = indices_reg[i][0]

        dois_pontos = string.find(":")

        if inicio_disp < inicio_reg:
            #Pega tudo desde o começo do dispositivo até o início do regulamento
            resultado = string[inicio_disp:inicio_reg]
            #Pega tudo desde o início do regulamento até encontrar ':'
            resultado3 = string[inicio_reg:dois_pontos]
            lista_dispositivos.append(resultado)
            lista_regulamentos.append(resultado3)
        elif inicio_disp > inicio_reg:
            #Pega tudo desde o início do dispositivo até encontrar ':'
            resultado2 = string[inicio_disp:dois_pontos]
            #Pega tudo desde o início do regulamento até o início do dispositivo
            resultado4 = string[inicio_reg:inicio_disp]
            lista_dispositivos.append(resultado2)
            lista_regulamentos.append(resultado4)
    print("Função regulamento - Encontrando o que é regulamento e o que é dispositivo : Finalizada")

    #Retirando informações que não fazem parte do regulamento que ficam no final do processo
    del lista_dispositivos[len(indices_disp):]
    del lista_regulamentos[len(indices_reg):]
    del descricao[len(indices_disp):]
    for item in enumerate(descricao):
      if not lista_dispositivos:
        lista_dispositivos.append("Erro")
      if not lista_regulamentos:
        lista_regulamentos.append("Erro")
    lista_dispositivos = [auxiliar.capitalize().strip().rstrip(',') for auxiliar in lista_dispositivos]
    lista_regulamentos = [auxiliar2.capitalize().strip().rstrip(',') for auxiliar2 in lista_regulamentos]
    descricao = [auxiliar3.capitalize().strip() for auxiliar3 in descricao]

    print("Função regulamento: Finalizada")
    return lista_regulamentos, lista_dispositivos, descricao
