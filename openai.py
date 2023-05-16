from urllib.request import urlopen
from urllib.request import Request
import json

print("**************CHAT GPT**************")
b = input("\nQual a pergunta?")

site = "https://api.openai.com/v1/chat/completions"
body = '{"model":"gpt-3.5-turbo","messages": [{"role": "user","content": "'+b+'"}],"temperature": 0.1}'
body = str.encode(body)

req = Request(site, data=body)
req.add_header('Authorization','Bearer apiKey')
req.add_header('Content-Type','application/json')
response = urlopen(req).read()
response = response.decode()
dados = json.loads(response)
resposta = dados['choices'][0]['message']['content']
print(resposta)
