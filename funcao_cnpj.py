from funcao_arrumar import arrumar
import re

def cnpj(celula):
    print("Função cnpj: Em andamento")
    arrumar(celula)
    celula_limpa = re.sub(r'[./\-) ]','',celula.text)
    celula_formatada = f"{celula_limpa[:2]}.{celula_limpa[2:5]}.{celula_limpa[5:8]}/{celula_limpa[8:12]}-{celula_limpa[12:]}"
    celula_final = re.sub(r'[,;]','',celula_formatada)
    print("Função cnpj: Finalizada")
    return celula_final
