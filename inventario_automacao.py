import pandas as pd

dados = {
"SKU": ["SKU001", "SKU002", "SKU003", "SKU004", "SKU005"],
"Produto": [
    "Shampoo Nutrição",
    "Condicionador",
    "Máscara Capilar",
    "Blush Rosé",
    "Batom Nude"
],

"Solicitado": [120, 80, 60, 150, 200],

"Enviado": [118, 80, 62, 150, 195],

"Recebido": [118, 78, 62, 150, 195]


}

df = pd.DataFrame(dados)

df["Divergência"] = df["Enviado"] - df["Recebido"]

df.to_excel("estoque_teste.xlsx", index=False)

print("Planilha criada com sucesso!")


