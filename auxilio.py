import requests
import json
from time import sleep
      
cpf = 00000000000 #COLOQUE SEU CPF AQUI
token = 000000 #COLOQUE O CODIGO DO SMS AQUI

url = "https://auxilio.caixa.gov.br/api/sms/validarLogin"
headers = {
    "content-type": "application/json; charset=utf-8"
}
payload = {
    "cpf": int(cpf)
 }
consulta = requests.post(url, headers=headers, data=json.dumps(payload))
msg = consulta.json()['mensagem'].upper()

if 'VÁLIDO' in msg:
    print(f'CPF => {cpf}')
    print(f'CÓDIGO DE ACESSO => {token}')
    sleep(1)
    print('ACESSANDO...')
    sleep(1)
    
    url_base = f"https://auxilio.caixa.gov.br/api/cadastro/validarLogin/{cpf}"
    headers = {
        "content-type": "application/json; charset=utf-8"
    }
    payload = {
        "token": f"{token}"
    }

    dados = requests.put(url_base, headers=headers, data=json.dumps(payload))
    dados = dados.json()

    if 'codigo' in dados:
        if dados['codigo'] == 401:
        	print('seu codigo de acesso está inválido'.upper())
        	exit()
    
    if dados:
        print('PEGANDO DADOS...')
        sleep(2)
        print(f"""RESULTADO:
            Nome: {dados['noPessoa']}
            CPF: {dados['cpf']}
            Situação: {dados['situacao']} | {dados['nuSituacaoCadastro']}
            Motivo: {dados['motivo']}
            Banco: {dados['banco']}
            Bolsa Família: {dados['bolsa_familia']}
            Solicitação inicial: {dados['dhFinalizacaoCadastro']}
            """.upper())
else:
    print('CÓDIGO DE ACESSO NÃO ESTÁ MAIS VÁLIDO!')
    print(msg)
            