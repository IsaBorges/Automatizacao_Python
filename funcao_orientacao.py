def orientacao(doc):
    print("Função orientação: Em andamento")
    for table in doc.tables:
        new_table = doc.add_table(rows = len(table.columns), cols = len(table.rows))

        for i, row in enumerate(table.rows):
            for j, cell in enumerate(row.cells):
                new_table.cell(j,i).text = cell.text

        parent = table._element.getparent()
        parent.remove(table._element)
        parent.append(new_table._element)
    print("Função orientação: Finalizada")
