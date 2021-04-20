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

#Retorna todos os grupos
def getGroups():
	r = requests.get(servidor+'group', 
		headers = headers)
	r = r.json()
	return r

# Cria uma task de multicast de acordo com o ID do grupo
def createMulticastTask(id):
	r = requests.post(servidor+'group/'+id+'/task', 
		headers = headers,
		data = json.dumps({"taskTypeID": 8}))
	return r

# Cria uma task de deploy de acordo com o ID do grupo
def createDeployGroup(id):
	r = requests.post(servidor+'group/'+id+'/task', 
		headers = headers,
		data = json.dumps({"taskTypeID": 1}))
	return r


# Retorna todos os tipos de task possiveis
def tipotask():
	r = requests.get(servidor+'tasktype', headers = headers)
	r = r.json()
	return r


if __name__ == '__main__':




	print('1 - Listar Hosts\n2 - Listar Imagens\n3 - Tasks ativas\n4 - Deploy\n5 - Captura\n6 - Excluir todas as task\n7 - Historico\n8 - Tipos de Task\n9 - Listar Grupos\n10 - Criar multicast\n11 - Deploy em grupo\n')


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
			host_id = input('Digite o ID do Host: ')
			r = deployByID(host_id)
			print(r)

		elif opcao == '5':
			host_id = input('Digite o ID do Host: ')
			r = captureByID(host_id)
			print(r)

		elif opcao == '6':
			r = deleteAllTask()
			print(r)

		elif opcao == '7':
			r = getHistoryHead()
			for i in range(len(r['historys'])-5, len(r['historys'])):
				print(r['historys'][i]['info'])

		elif opcao == '8':
			print('Tipo da Task:\n')
			r = tipotask()
			print(r['count'])
			for i in r['tasktypes']:
				print('---', i['id'], i['description'])

		elif opcao == '9':
			r = getGroups()
			print(r['count'], 'grupos')
			#print(r)
			for i in r['groups']:
				print( '------>ID:', i['id'], ' Nome:', i['name'], ' Numero de Hosts:', i['hostcount'])

		elif opcao == '10':
			group_id = input('Digite o ID do Grupo: ')
			r = createMulticastTask(group_id)
			print(r)

		elif opcao == '11':
			group_id = input('Digite o ID do Grupo: ')
			r = createDeployGroup(group_id)
			print(r)

		elif opcao == 't':
			print('Teste:\n')
			r = createDeployGroup(str(1))
			print(r)

		else:
			break

