from funcao_arrumar import arrumar
import re

def doc_comunicacao_judicializacao(celula):
    print("Função doc_comunicacao_judicializacao: Em andamento")
    #Regex para ignorar o que vem entre parenteses
    pdr_documento = re.sub(r'\([^)]*\)', '', celula.text)
    celula.text = pdr_documento
    arrumar(celula)
    print("Função doc_comunicacao_judicializacao: Finalizada")
    return celula.text
