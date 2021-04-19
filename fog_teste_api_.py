import requests
import json

# ? = Adicionar a api do usuario e a api do fog
headers = {
	'fog-api-token' : '?',
	'fog-user-token': '?'
}

# ? = Adicionar o endereco do servidor fog
servidor = 'http://?/fog/'


# Retorna todos os hosts 
def getAllHosts():
	r = requests.get(servidor+'host', headers = headers)
	r = r.json()
	return r


# Retorna todas as imagens
def getAllImages():
	r = requests.get(servidor+'image', 
		headers = headers)
	r = r.json()
	return r

# Retorna o historico de mudancas no fog
def getHistoryHead():
	r = requests.get(servidor+'history', headers = headers)
	r = r.json()
	return r

# Cria uma task de deploy para o host com o ID informado nos parametros
def deployByID(id):
	r = requests.post(servidor+'host/'+id+'/task', 
		headers = headers, 
		data = json.dumps({"taskTypeID": 1}))
	return r


# Cria uma task de captura de imagem para o host com o ID informado nos parametros
def captureByID(id):
	r = requests.post(servidor+'host/'+id+'/task', 
		headers = headers, 
		data = json.dumps({"taskTypeID": 2}))
	return r

# Deleta todas as task
def deleteAllTask():
	r = requests.delete(servidor+'task/cancel', 
		headers = headers)
	return r

# Retorna todas as tasks ativas
def getAllActivesTasks():
	r = requests.get(servidor+'task/current', 
		headers = headers)
	r = r.json()
	return r



if __name__ == '__main__':




	print('1 - Listar Hosts\n2 - Listar Imagens\n3 - Tasks ativas\n4 - Deploy\n5 - Captura\n6 - Excluir todas as task\n7 - Historico')


	while(True):

		opcao = input()

		if opcao == '1':
			r = getAllHosts()
			print(r['count'], 'hosts')
			for i in r['hosts']:
				print('------> Name:', i['name'], '  ID:', i['id'], '  ImageID', i['imageID'])

		elif opcao == '2':
			r = getAllImages()
			print(r['count'], 'imagens')
			for i in r['images']:
				print('------> Name:', i['name'], '  ID:', i['id'])

		elif opcao == '3':
			r = getAllActivesTasks()
			print(r['count'], 'tasks ativas')
			for i in r['tasks']:
				print('------>', i['id'], i['name'], i['createdTime'], i['state']['description'])

		elif opcao == '4':
			host_id = input('Deploy - Digite o ID do Host: ')
			status = deployByID(host_id)
			print(status)

		elif opcao == '5':
			host_id = input('Captura - Digite o ID do Host: ')
			status = captureByID(host_id)
			print(status)

		elif opcao == '6':
			status = deleteAllTask()
			print(status)

		elif opcao == '7':
			r = getHistoryHead()
			for i in range(len(r['historys'])-5, len(r['historys'])):
				print(r['historys'][i]['info'])
		else:
			break
