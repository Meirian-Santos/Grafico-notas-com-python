# Funções para análise de dados
"""
utils.py - Funções auxiliares para análise de dados escolares
"""

def media_coluna(df, coluna):
    """Calcula a média de uma coluna numérica do DataFrame."""
    return df[coluna].mean()

def valor_maximo(df, coluna):
    """Retorna o valor máximo da coluna especificada."""
    return df[coluna].max()

def valor_minimo(df, coluna):
    """Retorna o valor mínimo da coluna especificada."""
    return df[coluna].min()

def contar_registros(df):
    """Conta o número de registros (linhas) no DataFrame."""
    return len(df)
