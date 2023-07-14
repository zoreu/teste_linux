import requests
r = requests.get('https://github.com/zoreu/update_oneplay/raw/main/update.txt')
codigo = r.text
# print(codigo)
with open('exemplo_gerado.txt', 'w') as f:
    f.write(codigo)
print('arquivo gerado com sucesso!')
