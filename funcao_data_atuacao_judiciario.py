import re

def data_atuacao_judiciario(celula):
    print("Função data_atuacao_judiciario: Em andamento")
    padrao_data = r"\b\d{2}/\d{2}/\d{4}\b"
    data = re.findall(padrao_data, celula.text)
    
    if data:
      celula.text = data
    else:
      data = "Sem acesso à informação"
    print("Função data_atuacao_judiciario: Finalizada")
    return celula.text
