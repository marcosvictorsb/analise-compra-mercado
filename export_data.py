import csv
def export_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=';')
        csv_writer.writerow(['Número do Pedido', 'Data do Pedido', 'Total de Produtos', 'Taxa de Entrega', 'Valor Total', 'Situação', 'Tipo de Entrega', 'Observação', 'Nome do Produto', 'Quantidade', 'Preço Unitário', 'Valor Total Produto', 'Observação Produto'])
        csv_writer.writerows(data)