# ler os dados
file_path = "vendas.csv"
with open(file_path, mode="r", encoding="utf-8") as open_file:
    lines: str = open_file.readlines()
    

# processá-los em um dicionário para análise 
lines_dict = {}

keys: list = lines[0].strip("\n").split(",")
for key in keys:
    lines_dict[key] = []


for line in lines[1:]:
    values: list = line.strip("\n").split(",")
    lines_dict[key] = values[key]

    


# e, por fim, calcular e reportar as vendas totais por categoria de produto