import requests

# URL base da API

url = 'https://inepdata.inep.gov.br/analytics/saw.dll?Dashboard&PortalPath=%2Fshared%2FCenso%20da%20Educa%C3%A7%C3%A3o%20B%C3%A1sica%2F_portal%2FCat%C3%A1logo%20de%20Escolas&Page=Lista%20das%20Escolas&P1=dashboard&Action=Navigate&ViewState=306iq3horso6m27naqnckp1pde&P16=NavRuleDefault&NavFromViewID=d%3Adashboard~p%3Asf156n9k0qs70741'

# Fazer a solicitação GET
response = requests.get(url)

# Verificar o status da resposta
if response.status_code == 200:
    # A resposta foi bem sucedida, obter os dados
    data = response.json()
    # Faça algo com os dados...
    print(data)
else:
    # A solicitação falhou, lidar com o erro
    print('Falha na solicitação: {}'.format(response.status_code))
