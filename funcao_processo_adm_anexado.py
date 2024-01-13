from funcao_arrumar import arrumar
from funcao_retirar_caracteres import retirar_caracteres

def processo_adm_anexado(celula):
    print("Função processo_adm_anexado: Em andamento")
    celula.text = celula.text.replace(', ', ';')
    celula.text = celula.text.replace('e', ';')
    celula.text = celula.text.replace(' ', '')
    if ';' in celula.text:
        celula.text = celula.text.replace('\n', '')
    elif ';' not in celula.text:
        celula.text = celula.text.replace('\n', ';')

    arrumar(celula)
    retirar_caracteres(celula)
    print("Função processo_adm_anexado: Finalizada")
    return celula.text
