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

    # Exploratoria 1: ambos campos vacíos
def test_ambos_campos_vacios():
    resultado = autenticar_usuario("", "")
    assert resultado["success"] is False

# Exploratoria 2: usuario con espacios en blanco
def test_usuario_con_espacios():
    resultado = autenticar_usuario("   ", "1234")
    assert resultado["success"] is False

# Exploratoria 3: contraseña con espacios en blanco
def test_contrasena_con_espacios():
    resultado = autenticar_usuario("admin", "   ")
    assert resultado["success"] is False

# Exploratoria 4: mayúsculas/minúsculas
def test_usuario_mayusculas():
    resultado = autenticar_usuario("ADMIN", "1234")
    assert resultado["success"] is False

# Exploratoria 5: caracteres especiales
def test_usuario_caracteres_especiales():
    resultado = autenticar_usuario("@dm!n", "1234")
    assert resultado["success"] is False