from funcao_arrumar import arrumar

def vara(celula):
    print("Função vara: Em andamento")
    vara = celula.text.split('\n')
    vara_padrao = [item for item in vara if item.strip() != '']
    celula.text = vara_padrao[0]
    arrumar(celula)
    print("Função vara: Finalizada")
    return celula.text
