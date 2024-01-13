from funcao_arrumar import arrumar
import re

def status_processo_judicial(celula):
    print("Função status_processo_judicial: Em andamento")
    arrumar(celula)
    celula_limpa = re.sub(r'[.,;]','',celula.text)
    if celula_limpa == "Concluido" or celula_limpa == "Encerrado":
      celula_limpa = "Concluído"
    print("Função status_processo_judicial: Finalizada")
    return celula_limpa
