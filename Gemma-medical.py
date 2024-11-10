from ollama import Client

client = Client(host='http://localhost:11434')

# Reemplaza "llama2" con el nombre de tu modelo
response = client.chat(model='llama2:7b',
                      messages=[{'role': 'user', 'content': 'Hola, ¿cómo estás?'}])

print(response['message']['content'])