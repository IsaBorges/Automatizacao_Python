from funcao_arrumar import arrumar

def tipo_processo(celula):
    print("Função tipo_processo: Em andamento")
    tipologia_padrao = ["Ação Ordinária", "Ação Declaratória cumulada com anulatória", "Embargos à execução fiscal", 
                        "Mandado de Segurança", "Tutela antecipada antecedente"]
    arrumar(celula)
    duas_palavras = celula.text.split()[:2]
    for tipologia in tipologia_padrao:
      if duas_palavras == tipologia.split()[:2]:
        celula.text = tipologia
        
    print("Função tipo_processo: Finalizada")
    return celula.text
