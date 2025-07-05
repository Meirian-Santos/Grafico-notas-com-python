import pandas as pd
import matplotlib.pyplot as plt
from utils import media_coluna, valor_maximo, valor_minimo, contar_registros

# Lê o CSV
df = pd.read_csv("data.csv")

print("Número de registros:", contar_registros(df))
print("Média das notas:", media_coluna(df, "Nota"))
print("Média das idades:", media_coluna(df, "Idade"))

coluna = input("Qual coluna deseja verificar (Nota ou Idade)? ").capitalize()

if coluna in df.columns:
    print("Maior", coluna + ":", valor_maximo(df, coluna))
    print("Menor", coluna + ":", valor_minimo(df, coluna))
else:
    print("Coluna inválida. Use 'Nota' ou 'Idade'.")

# Gera gráfico de barras
plt.figure(figsize=(8, 5))
plt.bar(df["Nome"], df["Nota"], color="skyblue")
plt.title("Notas dos Alunos")
plt.xlabel("Nome")
plt.ylabel("Nota")
plt.tight_layout()
plt.savefig("grafico_notas.png")
plt.close()

