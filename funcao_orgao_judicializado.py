from funcao_arrumar import arrumar

def orgao_judicializado(celula):
    print("Função orgao_judicializado: Em andamento")
    arrumar(celula)
    #if celula.text[-1] != ')':
      #celula.text += ')'
    #else:
      #pass
    print("Função orgao_judicializado: Finalizada")
    return celula.text
