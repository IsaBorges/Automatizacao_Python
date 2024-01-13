import re


def retirar_caracteres(celula):
    padrao = r'[,;.]'

    if celula.text != '':
      ultimo_caracter = celula.text[-1]
      if re.search(padrao, ultimo_caracter):
        celula.text = celula.text[:-1]
      else:
        pass
