import os
import pandas as pd

print(os.getcwd())

planilha_bitcoin = pd.read_excel("csv/BTC-EUR.xlsx")

# print(planilha_bitcoin)

# DONE: Valor médio deve ser (High + Low) / 2
# Pegar os valores de High e Low da planilha
highs = planilha_bitcoin["High"]
lows = planilha_bitcoin["Low"]
# print(highs.shape)
# print(lows.shape)

# Calcular valor médio e colocar na planilha
planilha_bitcoin["Medio"] = (highs + lows) / 2

print(planilha_bitcoin["Medio"])


# TODO: Valor MA5 deve ser (Soma dos últimos 5 dias) / 5
planilha_bitcoin["MA5"] = planilha_bitcoin["Medio"]

teste = planilha_bitcoin[['Medio', 'MA5']]
print('primeira iteração')
print(teste)

for i in range(0, len(planilha_bitcoin)):
    if i < 5:
        planilha_bitcoin.loc[i, "MA5"] = 0
    else:
        planilha_bitcoin.loc[i, "MA5"] = (planilha_bitcoin.loc[i, "Medio"] + planilha_bitcoin.loc[i-1, "Medio"] + planilha_bitcoin.loc[i-2, "Medio"] + planilha_bitcoin.loc[i-3, "Medio"] + planilha_bitcoin.loc[i-4, "Medio"]) / 5

teste = planilha_bitcoin[['Medio', 'MA5']]
print('segunda iteração')
print(teste.iloc[5:10])

# Valor Open.1 deve ser (Open - (Medio - 1)) / Medio - 1
planilha_bitcoin["Open.1"] = 0

for i in range(0, len(planilha_bitcoin)):
    if i >= 1:
        planilha_bitcoin.loc[i, "Open.1"] = (planilha_bitcoin.loc[i, "Open"] - planilha_bitcoin.loc[i-1, "Medio"]) / planilha_bitcoin.loc[i-1, "Medio"]

print('verificando Open.1')
print(planilha_bitcoin["Open.1"])

# Valor High.1 deve ser (High - (Medio - 1)) / Medio - 1
planilha_bitcoin["High.1"] = 0

for i in range(0, len(planilha_bitcoin)):
    if i >= 1:
        planilha_bitcoin.loc[i, "High.1"] = (planilha_bitcoin.loc[i, "High"] - planilha_bitcoin.loc[i-1, "Medio"]) / planilha_bitcoin.loc[i-1, "Medio"]

print('verificando High.1')
print(planilha_bitcoin["High.1"])

# Valor Low.1 deve ser (Low - (Medio - 1)) / Medio - 1
planilha_bitcoin["Low.1"] = 0

for i in range(0, len(planilha_bitcoin)):
    if i >= 1:
        planilha_bitcoin.loc[i, "Low.1"] = (planilha_bitcoin.loc[i, "Low"] - planilha_bitcoin.loc[i-1, "Medio"]) / planilha_bitcoin.loc[i-1, "Medio"]

print('verificando Low.1')
print(planilha_bitcoin["Low.1"])

# Valor Close.1 deve ser (Close - (Medio - 1)) / Medio - 1
planilha_bitcoin["Close.1"] = 0

for i in range(0, len(planilha_bitcoin)):
    if i >= 1:
        planilha_bitcoin.loc[i, "Close.1"] = (planilha_bitcoin.loc[i, "Close"] - planilha_bitcoin.loc[i-1, "Medio"]) / planilha_bitcoin.loc[i-1, "Medio"]

print('verificando Close.1')
print(planilha_bitcoin["Close.1"])

# Valor Medio.1 deve ser (Medio - (Medio - 1)) / Medio - 1
planilha_bitcoin["Medio.1"] = 0

for i in range(0, len(planilha_bitcoin)):
    if i >= 1:
        planilha_bitcoin.loc[i, "Medio.1"] = (planilha_bitcoin.loc[i, "Medio"] - planilha_bitcoin.loc[i-1, "Medio"]) / planilha_bitcoin.loc[i-1, "Medio"]

print('verificando Medio.1')
print(planilha_bitcoin["Medio.1"])

# Valor MA5.1 deve ser (MA5 - (Medio - 1)) / Medio - 1
planilha_bitcoin["MA5.1"] = 0

for i in range(0, len(planilha_bitcoin)):
    if i >= 5:
        planilha_bitcoin.loc[i, "MA5.1"] = (planilha_bitcoin.loc[i, "MA5"] - planilha_bitcoin.loc[i-1, "Medio"]) / planilha_bitcoin.loc[i-1, "Medio"]

print('verificando MA5.1')
print(planilha_bitcoin["MA5.1"])

# DONE: Tirar as médias dos valores Open.1, High.1, Low.1, Close.1, Medio.1, MA5.1 
meanOpen1 = planilha_bitcoin["Open.1"].mean()
meanHigh1 = planilha_bitcoin["High.1"].mean()
meanLow1 = planilha_bitcoin["Low.1"].mean()
meanClose1 = planilha_bitcoin["Close.1"].mean()
meanMedio1 = planilha_bitcoin["Medio.1"].mean()
meanMa51 = planilha_bitcoin["MA5.1"].mean()

# DONE: Tirar o Desvio Padrão (StdDev) dos valores Open.1, High.1, Low.1, Close.1, Medio.1, MA5.1 
stdOpen1 = planilha_bitcoin["Open.1"].std()
stdHigh1 = planilha_bitcoin["High.1"].std()
stdLow1 = planilha_bitcoin["Low.1"].std()
stdClose1 = planilha_bitcoin["Close.1"].std()
stdMedio1 = planilha_bitcoin["Medio.1"].std()
stdMa51 = planilha_bitcoin["MA5.1"].std()