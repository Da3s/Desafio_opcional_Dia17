import requests


# 1.- Obtenga toda la información de los usuarios retornada por la API, guárdela en una variable llamada users_data e imprímala en pantalla.

# Se obtiene la informacion desde el enlace
response_get = requests.get("https://reqres.in/api/users")
# Se guarda todo en la variable users_data
users_data = response_get.json()
# Se imprime el resultado guardado en la variable users_data
print("Se imprime informacion de usuarios")
print(users_data)
print(response_get)


# 2.- Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el diccionario de respuesta en una variable llamada created_user e imprímala en pantalla

# Se crea usuario
payload_post = {
    "name": "Ignacio",
    "job": "Profesor"
}  
headers = {
'Content-Type': 'application/json'
}
# Se utiliza el metodo post para añadir el usuario
response_post = requests.post("https://reqres.in/api/users", headers=headers, json=payload_post)
# Se guarda en variable created_user
created_user = response_post.json()
# Se imprime resultado
print("Se creo un nuevo usuario")
print(created_user)
print(response_post)


# 3.- Actualice un usuario llamado morpheus para que tenga un campo llamado residence igual a zion. Guarde el diccionario de respuesta en una variable llamada updated_user e imprímala en pantalla. 

# Añadir usuario morpheus ya que no existe
payload_add = {
    "name": "morpheus"
}
headers = {
    'Content-Type': 'application/json'
}

response_add = requests.post("https://reqres.in/api/users", headers=headers, json=payload_add)
created_user3 = response_add.json()
print("Usuario añadido:")
print(created_user3)

# Actualizar usuario morpheus con campo residence igual a zion
payload_update = {
    "residence": "zion"
}

response_update = requests.put(f"https://reqres.in/api/users/{created_user3['id']}", headers=headers, json=payload_update)
updated_user3 = response_update.json()
print("Usuario actualizado:")
print(updated_user3)


# 4.- Elimine un usuario llamado Tracey. Imprima el código de respuesta en pantalla. 

response = requests.delete("https://reqres.in/api/users/7")
print("Código de respuesta al eliminar usuario Tracey:", response.status_code)