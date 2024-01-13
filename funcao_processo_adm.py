from funcao_arrumar import arrumar
import re

def processo_adm(celula):
    print("Função processo_adm: Em andamento")
    arrumar(celula)

    celula_filtrada = re.sub(r'[^0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]', '', celula.text)

    if '-' in celula_filtrada:
        texto_novo = celula_filtrada[:-3]
        celula_filtrada = texto_novo
    celula_filtrada = celula_filtrada.replace('.', '')
    celula_filtrada = celula_filtrada.replace('/', '')
    print("Função processo_adm: Finalizada")
    return celula_filtrada
