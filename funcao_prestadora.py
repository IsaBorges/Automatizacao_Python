from funcao_arrumar import arrumar
import re


def prestadora(celula):
    print("Função prestadora: Em andamento")
    prestadoras = ["ALGAR TELECOM S.A.", "CLARO S.A.", "EMPRESA BRASILEIRA DE TELECOMUNICACOES S.A.", "GLOBAL VILLAGE TELECOM S.A.",
                   "OI S.A.", "SERCOMTEL S.A. TELECOMUNICAÇÕES", "SKY BRASIL SERVIÇOS LTDA.", "TELEFÔNICA BRASIL S.A.",
                   "TELEMAR NORTE LESTE S.A.", "TIM CELULAR S.A", "TNL PCS S.A."]

    celula.text = celula.text.upper()
    celula.text = re.sub(r'[.,"\'-?:!;]', '', celula.text)
    primeira_palavra = celula.text.split()[0]

    if primeira_palavra == "TELEFONICA":
        primeira_palavra = "TELEFÔNICA"

    for palavra in prestadoras:
        if primeira_palavra == palavra.split()[0]:
            celula.text = palavra

    arrumar(celula)
    print("Função prestadora: Finalizada")
    return celula.text
