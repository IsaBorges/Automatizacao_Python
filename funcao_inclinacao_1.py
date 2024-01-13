from funcao_arrumar import arrumar

def inclinacao_1(celula):
    print("Função data_1_instancia: Em andamento")
    padrao_inclinacao = ['Desfavorável à Anatel', 'Favorável à Anatel', 'Parcialmente desfavorável à Anatel']
    info = celula.text.split()
    inclinacao = "-"
    inclinacao_teste = "-"
    # se houver outra data mais recente vai ser usada a primeira que se encaixa no padrão (Data: x)
    for cont in range(len(info)):
      if info[cont] == "Inclinação:":
        inclinacao_teste = info[cont+1].split()
    
    for aux in padrao_inclinacao:
      primeira = aux.split()[:1]
      if inclinacao_teste == aux.split()[:1]:
        inclinacao = aux
    
    print("Função data_1_instancia: Finalizada")
    return inclinacao
