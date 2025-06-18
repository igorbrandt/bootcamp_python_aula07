from etl import csv_reader, filter_products_by_delivery, sum_price_from_filtered_products

file_path = "vendas.csv"

products = csv_reader(file_path)
products_delivered = filter_products_by_delivery(products)
delivered_products_value = sum_price_from_filtered_products(products_delivered)
print(delivered_products_value)