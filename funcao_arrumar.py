def arrumar(celula):
    print("Função arrumar: Em andamento")
    texto = celula.text.replace('/t','')
    texto_arrumado = ' '.join(texto.split()).strip()
    celula.text = texto_arrumado
    print("Função arrumar: Finalizada")
