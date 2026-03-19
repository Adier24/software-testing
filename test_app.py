from app import autenticar_usuario
import time

def test_login_exitoso():
    resultado = autenticar_usuario("admin", "1234")

    assert resultado["success"] == True
    assert resultado["message"] == "Acceso concedido"
    assert resultado["response_time_ms"] > 0


def test_usuario_vacio():
    resultado = autenticar_usuario("", "1234")

    assert resultado["success"] == False
    assert resultado["message"] == "Usuario y contraseña son requeridos"


def test_contrasena_vacia():
    resultado = autenticar_usuario("admin", "")

    assert resultado["success"] == False
    assert resultado["message"] == "Usuario y contraseña son requeridos"


def test_usuario_inexistente():
    resultado = autenticar_usuario("pedro", "1234")

    assert resultado["success"] == False
    assert resultado["message"] == "Usuario no existe"


def test_contrasena_incorrecta():
    resultado = autenticar_usuario("admin", "9999")

    assert resultado["success"] == False
    assert resultado["message"] == "Contraseña incorrecta"


from app import autenticar_usuario 
def test_tiempo_respuesta_login_exitoso(): 
    inicio = time.perf_counter() 
    resultado = autenticar_usuario("admin", "1234")     
    fin = time.perf_counter() 

    tiempo_ms = (fin - inicio) * 1000 

    assert resultado["success"] == True 
    assert tiempo_ms < 500

from app import autenticar_usuario 
def test_tiempo_reportado_por_el_sistema(): 
    resultado = autenticar_usuario("admin", "1234") 
    
    assert resultado["response_time_ms"] > 0
    assert resultado["response_time_ms"] < 500 

#-------------------------------------------------------------------------------------------

