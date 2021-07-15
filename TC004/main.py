import requests
import pandas as pd
from credentials import token

# Para propósitos de leitura de outros arquivos, se necessário.
arquivo="TC004\\repasses.xlsx"

# Faz a leitura da planilha com os dados 
raw_data = pd.read_excel(arquivo)

# Converte para json para realizar o envio
json_data = raw_data.to_json(orient="records", date_format="iso")

# Headers da requisição com o token de autenticação em outro arquivo
headers = {
    "content-type": "application/json",
    "token": token
}

r = requests.post(f"https://sistema.trackcash.com.br/api/mkp/payments", data=json_data, headers=headers)

# Para verificar o status da requisição
"""if r.status_code == 200:
    print("OK")
else:
    print(f"Erro {r.status_code}")"""
