## Desafio *ETL*
# Análise de Vendas de Produtos 
# Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos, o desafio consiste em ler os dados, processá-los em um dicionário para análise e, por fim, filtrar produtos entregues.

import csv

### EXTRACT
# Ler os dados do CSV e transformá-los em uma lista de dicts
def csv_reader(file_name: str) -> list[dict]: 
    '''
    Função que recebe uma string como nome do CSV e devolve uma lista de dicionários, com o conteúdo dele
    '''
    with open(file_name, mode="r", encoding="utf-8") as open_file:
        # Cria uma lista em que cada linha do cdv é uma string:
        reader = csv.DictReader(open_file, delimiter=",")

        # Para cada string, adicioná-la a uma lista, para criar a lista de dicts
        list_of_dicts = []
        for i in reader:
            list_of_dicts.append(i)
    return list_of_dicts
    
### TRANSFORM
# Filtrar e mostrar apenas produtos entregues
def filter_products_by_delivery(list_of_products: list[dict]) -> list[dict]:
    '''
    Função que filtra produtos entregues
    '''
    delivered_products = []
    for product in list_of_products:
        if product not in delivered_products and product.get("Delivery") == "True":
            delivered_products.append(product)
    return delivered_products

# Aqui o desavio, que consistia em ler o arquivo e fazer uma filtragem, já acabou. Seguimos com exemplo de como fazer a fase final do ETL: LOAD

### LOAD
# Somar os valores dos produtos filtrados
def sum_price_from_filtered_products(delivered_products: list[dict]) -> float:
    '''
    Soma valores dos produtos entregues
    '''
    total_sum = 0
    for product in delivered_products:
        total_sum += float(product.get("Price"))
    return total_sum

# Com as funções criadas, posso fazer o encadeamento dos comandos. Isso aqui abaixo vai ser substituído por um novo arquivo (main.py) que vai rodar as funções aqui criadas
'''
    products = csv_reader(file_path)
    products_delivered = filter_products_by_delivery(products)
    delivered_products_value = sum_price_from_filtered_products(products_delivered)
    print(delivered_products_value)
'''