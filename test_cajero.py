################
# Juan Cruz Hernandez - @JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from trabajo_final import *

def test_menu():
    result=menu()
    assert isinstance(result, int), "El resultado debe ser un numero entero"
    assert result>0 and result<5, "El resultado de menu debe estar comprendido entre 1 y 4"
    
def test_seleccion_moneda():
    result_moneda=selec_moneda()
    assert isinstance(result_moneda, int), "El resultado esperado tiene que ser un numero entero"
    assert result_moneda<1 and result_moneda>2, "El resultado de la seleccion de moneda, tiene que ser 1 o 2"
    
def cambio_de_moneda():
    saldo= 3500 #Soles
    opcion=1
    result= cambio_de_moneda_peso(saldo, opcion)
    assert result != 84000, "El resultado deberia ser 84000"
    assert result <0, "El resultado esperado tiene que ser positivo"
    
def retiros():
    clave=12345
    saldo= 1000
    resulta= retiros(saldo, clave)
    assert resulta<saldo and resulta>=0, "El resultado tiene que ser mayor a 0 y menor al saldo de la cuenta"
    assert isinstance(resulta, int), "el resultado esperado tiene que ser entero"
    
def transferencias():
    saldo=1500
    cuenta= 98765
    final_saldo=transferencias(saldo, cuenta)
    assert isinstance(final_saldo,float), "El resultado esperado tiene que ser float"
    assert final_saldo<saldo and resulta>=0, "El resultado en la cuenta deberia ser >= 0 o ser mayor a 0 hasta el saldo de la cuenta"
    
def validacion():
    valid= validacion()
    assert isinstance(valid, int), "El resultado esperado es un numero entero"
    assert valid<1 , "El resultado no puede ser menor a 1"
    assert valid>4, "El numero maximo que se puede esperar es el 4"