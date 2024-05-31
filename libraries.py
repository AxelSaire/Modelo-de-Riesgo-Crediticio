import re
import pandas as pd
import numpy as np

def ordenar(categorias):
    """
    Ordena una lista de categorías que contienen números al principio.
    
    Args:
        categorias (list of str): Lista de categorías a ordenar.
        
    Returns:
        list of str: Lista de categorías ordenadas.
    """
    numeros_categorias = [(float(re.split(r'-', cat)[0]), cat) for cat in categorias]
    numeros_categorias.sort(key=lambda x: x[0])
    categorias_ordenadas = [cat for _, cat in numeros_categorias]
    
    return categorias_ordenadas
