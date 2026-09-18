import configuration
import requests
import data

# -----------------------------------> METODOS GET <-------------------------------------

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# -----------------------------------> METODOS POST <-------------------------------------
def post_new_user(body):
    new_header = data.headers.copy()
    new_header.pop("Authorization")
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=new_header)  # inserta los encabezados

def create_header_authorization(auth_token):
    current_header = data.headers.copy()
    current_header["Authorization"] += auth_token
    return current_header

def post_new_client_kit(kit_body,auth_token):
    new_header = create_header_authorization(auth_token)
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json = kit_body,
                         headers = new_header)