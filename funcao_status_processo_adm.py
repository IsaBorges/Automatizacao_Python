from funcao_arrumar import arrumar
import re

def status_processo_adm(celula):
    print("Função status_processo_adm: Em andamento")
    arrumar(celula)
    celula_limpa = re.sub(r'[.,;]','',celula.text)
    if celula_limpa == "Concluido" or celula_limpa == "Encerrado":
      celula_limpa = "Concluído"
    print("Função status_processo_adm: Finalizada")
    return celula_limpa
