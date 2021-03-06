import sys

clients = [
  {
    'name': 'Pablo',
    'company': 'Google',
    'email': 'pablo@google.com',
    'position': 'Software engineer',
  },
  {
    'name': 'Ricardo',
    'company': 'Facebook',
    'email': 'ricardo@facebook.com',
    'position': 'Data engineer',
  }
]

#CREATE
def create_client(client):
  global clients

  if client not in clients:
    clients.append(client)
  else:
    print('Client already is in the client\'s list')


#LIST
def list_clients():
  for idx, client in enumerate(clients):
    print('{uid} | {name} | {company} | {email} | {position}'.format(
      uid=idx,
      name=client['name'],
      company=client['company'],
      email=client['email'],
      position=client['position']
    ) )


#UPDATE
def update_client(client_id, updated_client):#RECIBE EL INDICE Y LOS DATOS A CAMBIAR
  global clients

  if len(clients) - 1 == client_id:
    clients[client_id] = updated_client
  else:
    print('Client is not in clients list')


#DELETE
def delete_client(client_id):
  global clients

  # for idx, client in enumerate(clients):
  #   if idx == client_id:
  #     del clients[idx]
  #     list_clients()
  #     break
  if client_id == 0:
    clients.pop(0)
  elif len(clients) - 1 == client_id:
    clients.remove(clients[client_id])
  else:
    print('Client is not in clients list')


#SEARCH
def search_client(client_name):
  for client in clients:
    if client['name'] != client_name:
      continue
    else:
      return True

#SOLICITA DATOS PARA CREAR CLIENTE (DICCIONARIO)
def _get_client_field(field_name):
  field = None

  while not field:
    field = input('What is the client {}?'.format(field_name))
  return field


#CREA UN CLIENTE PARA HACER UPDATE
def _get_client_from_user():
  client = {
      'name': _get_client_field('name'),
      'company': _get_client_field('company'),
      'email': _get_client_field('email'),
      'position': _get_client_field('position'),
    }
  return client


#SOLISITA NOMBRE DE CLIENTE
def _get_client_name():
  client_name = None

  while not client_name:
    client_name = input('What is the client name?: ')
    if client_name == 'exit':
      client_name = None
      break

  if not client_name:
    sys.exit()

  return client_name

#MENU
def _print_welcome():
  print('WELCOME TO PLATZI VENTAS')
  print('*' * 50)
  print('What would you like to do today?')
  print('[C]reate client')
  print('[L]ist clients')
  print('[U]pdate client')
  print('[D]elete client')
  print('[S]earch client')


if __name__ == '__main__':
  _print_welcome()

  command = input()
  command = command.upper()

  if command == 'C':
    client = {
      'name': _get_client_field('name'),
      'company': _get_client_field('company'),
      'email': _get_client_field('email'),
      'position': _get_client_field('position'),
    }
    #client_name = _get_client_name()
    create_client(client)
    list_clients()
  elif command == 'L':
    list_clients()
  elif command == 'D':
    list_clients()
    client_id = int(_get_client_field('id'))
    
    delete_client(client_id) 
    list_clients()
  elif command == 'U':
    list_clients()
    client_id = int(_get_client_field('id'))
    updated_client = _get_client_from_user()

    update_client(client_id, updated_client)
    list_clients()
  elif command == 'S':
    client_name = _get_client_field('name')
    print(client_name)
    found = search_client(client_name)

    if found:
      print('The client is in the client\'s list')
    else:
      print('The client: {} is not in our client\'s list'.format(client_name))
  else:
    print('Invalid command')