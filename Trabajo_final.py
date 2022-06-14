import random
import time

def menu():
    """
    Esta funcion se encarga de mostrar el menu
    """
    print("**********************")
    print("**********************")
    print("1. Consultas")
    print("2. Retiros ")
    print("3. Transferencias")
    print("4. Salir")
    print("**********************")
    print("**********************")
    opcion=int(input(""))
    while opcion<0 or opcion>4:
        opcion=int(input("Ingrese un valor valido del menu: "))
    return opcion

def selec_moneda():
    """
    Esta funcion se encarga de preguntar que moneda desea utilizar
    """
    print("Seleccione el tipo de moneda")
    print("1. Soles      2. Pesos")
    opcion= int(input(""))
    while opcion<1 or opcion>2:
        opcion=int(input("Ingrese un valor valido del menu"))
    return opcion

def cambio_de_moneda_peso(saldo_cuenta, opcion):
    """
    Esta funcion se encarga de hacer la conversion de la moneda
    """
    pesos=24  #Se multiplica por 24 Para que de como resultado 85.000 o el resultado en pesos pedido
    if opcion==1:
        resulta= saldo_cuenta*pesos
    else:
        resulta= saldo_cuenta/pesos
    return resulta

def volver():
    print("Volviendo al menu..")
    time.sleep(1)

def consultas(saldo_cuenta):
    """
    Este procedimiento se encarga de mostar el saldo de la cuenta
    y los ultimos 10 movimientos
    """
    randomi=["Transferencia", "Extraccion"]
    saldo= saldo_cuenta
    print("1. Posicion global")
    print("2. Movimientos")
    opcion=int(input())
    while opcion<1 or opcion>2:
        opcion=int(input("Ingrese un valor valido del menu"))
    if opcion==1:
        pesos= selec_moneda()
        if pesos==1:
            print(f"Usteded tiene {saldo} en Soles Peruanos")
        else:
            saldo= cambio_de_moneda_peso(saldo, 1)
            print(f"Usted tiene {saldo} en Pesos Argentinos")
    else:
        print("Ultimos movimientos: ")
        for i in range (10):
            print(random.choice(randomi),"de:", random.randint(1,150), "pesos")
    volver()           

def retiros(saldo_cuenta,clave):#Parametros de entrada: saldo_cuenta, clave
    """
    Esta funcion se encarga de controlar los retiros de la cuenta
    """
    clave_original=clave
    pesos= selec_moneda()
    if pesos== 1:
        print("Monto a retirar en soles: ")
        monto= float(input(""))
    else:
        print("Monto a retirar en pesos: ")
        monto= float(input(""))
        #monto= cambio_de_moneda_peso(monto,1) # Invocacion para trabajar con pesos argentinos
        saldo_cuenta= cambio_de_moneda_peso(saldo_cuenta,1) # Cambia todo el monto a pesos argentinos
    if monto> saldo_cuenta:
        print("El monto a retirar no es correcto")
        print(f"Recuerde que el saldo en la cuenta es: {saldo_cuenta}")
        monto= float(input("Ingrese el monto: "))
    if monto>0 and monto<saldo_cuenta:
        print("Ingrese la clave de acceso:")
        clave=int(input(""))
        if clave==clave_original:
            saldo_cuenta= saldo_cuenta - monto
            print("desea imprimir comprobante?: ")
            print("1. Si     2. No")
            comprobante= int(input(""))
            if comprobante==1:
                print(f"Monto retirado: {monto}")
                print(f"Saldo en la cuenta: \n{saldo_cuenta}")
            saldo_cuenta= cambio_de_moneda_peso(saldo_cuenta,2)
    volver()
    return saldo_cuenta

def transferencias(saldo, cuenta):
    """
    Esta funcion se encarga de mostrar realizar transferencias a otras cuentas
    """
    cuenta_trans= cuenta
    print("Ingrese cuenta a la que se quiere transferir:")
    cuenta_destino=int(input(""))
    moneda= selec_moneda()
    if moneda==1:
        print("Monto a transferir en soles:")
        monto=float(input(""))
    else:
        print("Monto a transferir en pesos:")
        monto= float(input(""))
        monto=cambio_de_moneda_peso(monto, 1)
        saldo=cambio_de_moneda_peso(saldo, 1)
    if monto> saldo:
        print("el monto igresado no es valido, no tiene los fundos suficientes")
    else:
        print("Realizando Transferencia")
        i=0
        while i<5:
            print("...")
            i+=1
            time.sleep(1)
        print("Transferencia exitosa")
        time.sleep(2)
        saldo= saldo-monto
    volver()
    return saldo


def validacion():
    cont=0
    i=0
    clave= 12345
    dni=12345678
    print("recopilando informacion")
    while i<5:
        print("...")
        i+=1
        time.sleep(1)
    print("Ingrese clave de acceso:")
    cla_ingresada= int(input(""))
    while clave!=cla_ingresada and cont<3:
            print("ingrese clave correcta: ")
            cla_ingresada= int(input())
            cont+=1
    if cla_ingresada==clave:
        print("Ingrese numero de documento: ")
        documento= int(input())
        while dni!=documento and cont<3:
            print("ingrese documento correcto: ")
            documento= int(input())
            cont+=1
    if documento==dni and cla_ingresada==clave:
        opcion=0
    else:
        print("clave/dni incorrectos se retendra la tarjeta")
        opcion=4
    return opcion
        
def principal():
 
    saldo_en_cuenta=3564 #soles
    clave= 12345
    dni=12345678
    cuenta= 98765
    print("Ingrese tarjeta en la ranura:")
    opcion=validacion()
    while opcion!=4:
        opcion= menu()
        if opcion==1:
            consultas(saldo_en_cuenta)
        elif opcion==2:
            saldo_en_cuenta=retiros(saldo_en_cuenta, clave)
        elif opcion==3:
            saldo_en_cuenta=transferencias(saldo_en_cuenta, cuenta)
    
principal()
