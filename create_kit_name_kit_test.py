import sender_stand_request
import data

# esta función cambia los valores en el parámetro "name"
def get_kit_body(name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    token = response.json()["authToken"]
    return token

def positive_assert(kit_body):
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400

#PRUEBA 1
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

#PRUEBA 2
def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)

#PRUEBA 3
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

#PRUEBA 4
def test_create_kit_512_letter_in_name_get_error_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)

#PRUEBA 5
def test_create_kit_has_special_symbol_in_name_get_success_response():
    kit_body = get_kit_body("\"№%@\",")
    positive_assert(kit_body)

#PRUEBA 6
def test_create_kit_has_space_in_name_get_success_response():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

#PRUEBA 7
def test_create_kit_has_numbers_in_name_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

#PRUEBA 8
def test_create_kit_when_name_no_exist_get_error_response():
    kit_body = {}
    negative_assert_code_400(kit_body)

#PRUEBA 9
def test_create_kit_has_number_in_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)