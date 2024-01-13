from funcao_arrumar import arrumar

def data_decisao_liminar(celula):
    print("Função data_decisao_liminar: Em andamento")
    arrumar(celula)
    info = celula.text.split()
    data = "Sem acesso à informação"
    #se houver outra data mais recente vai ser usada a primeira que se encaixa no padrão (Data: x)
    for cont in range(len(info)):
        if info[cont] == "Data:":
            data = info[cont+1]
            break
    print("Função data_decisao_liminar: Finalizada")
    return data
