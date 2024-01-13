from funcao_arrumar import arrumar
import re

def servico(celula):
    print("Função servico: Em andamento")
    servico_padrao = ["Serviço de Acesso Condicionado (SeAC)","Serviço de Comunicação Multimídia (SCM)",
                      "Serviço de Distribuição de Sinais de Televisão e de Áudio por Assinatura Via Satélite (DTH)",
                      "Serviço Móvel Pessoal (SMP)","Serviço Telefônico Fixo Comutado (STFC)"]
    arrumar(celula)
    tres_palavras = celula.text.split()[:3]
    for service in servico_padrao:
      if tres_palavras == service.split()[:3]:
        celula.text = service

    print("Função servico: Finalizada")
    return celula.text
