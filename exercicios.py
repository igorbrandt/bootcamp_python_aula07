from typing import List

### 1. Calcular Média de Valores em uma Lista
def calcular_media_de_valores(valores_para_calcular_media: List[float]) -> List[float]:
    return sum(valores_para_calcular_media)/len(valores_para_calcular_media)

print(calcular_media_de_valores([2.4,7,99,0,-5,-6.3]))

### 2. Filtrar Dados acima de um limite.
def filtrar_valores(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

print(filtrar_valores([1,3,-7,74,0,3.5],0))

### 3. Contar Valores Únicos em uma Lista
def contar_valores_unicos_na_lista(valores_para_contar: List[float]) -> int:
    return len(set(valores_para_contar))

print(contar_valores_unicos_na_lista([2.1,5,7,2.1,9,8,7,0,-3]))

### 4. Converter Celsius para Fahrenheit em uma Lista
def converter_graus_celcius_para_fahrenheit(temperatura_em_celcius: float) -> float:
    return temperatura_em_celcius * 1.8 + 32

print(converter_graus_celcius_para_fahrenheit(30))

### 5. Calcular Desvio Padrão de uma Lista
def calcular_desvio_padrao(lista_para_calcular_desvio_padrao: List[float]) -> float:



### 6. Encontrar Valores Ausentes em uma Sequência