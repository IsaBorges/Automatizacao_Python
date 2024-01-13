from funcao_arrumar import arrumar
import re
def processo_judicial(celula):
    print("Função processo_judicial: Em andamento")
    arrumar(celula)
    processos = celula.text.split()
    processo_associado = []
    i = 0

    print("Função processo_judicial - Para pegar processos associados: Em andamento")
    #Loop para pegar o número dos processos associados que vem antes da frase (processo judicial associado)
    while i <= len(processos) - 3:
        if processos[i] == "(processo" and processos[i+1] == "judicial" and processos[i+2] == "associado)":
            processo_associado.append(processos[i-1])
            i += 3
        else:
            i += 1

    #Juntar todos os processos associados em uma string
    processo_join = '; '.join(processo_associado)
    print("Função processo_judicial - Para pegar processos associados: Finalizada")
    print("Função processo_judicial - Para pegar o processo principal: Em andamento")
    #O processo principal é a primeira coisa a aparecer na célula, por isso o uso do .split[0]
    celula.text = celula.text.split()[0]
    celula_limpa = re.sub(r'[./\-) ]','',celula.text)
    celula_formatada = f"{celula_limpa[:7]}-{celula_limpa[7:9]}.{celula_limpa[9:13]}.{celula_limpa[13:14]}.{celula_limpa[14:16]}.{celula_limpa[16:20]}"
    
    print("Função processo_judicial - Para pegar o processo principal: Finalizada")
    print("Função processo_judicial: Finalizada")
    return celula_formatada, processo_join
