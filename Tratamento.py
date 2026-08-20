import pandas as pd

# Carregar a planilha
#COLOQUE SUA PLANILHA AQUI
df = pd.read_excel("Ticket.xlsx")

# Extrair apenas a primeira palavra da coluna de Pretensão
df["Pretensao"] = df["Pretensão"].str.split().str[0]

# Agrupar por Unidade, Ano, Mes e Pretensão
agrupado = df.groupby(["Unidade", "Ano", "Mes", "Pretensao"]).size().reset_index(name="Quantidade")

# Salvar em uma nova planilha
agrupado.to_excel("dados_separados_mes_ano.xlsx", index=False)

print("Planilha gerada com sucesso!")
