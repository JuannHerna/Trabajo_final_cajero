# Trabajo_final_cajero
Clave: 12345

DNI: 12345678

Cuenta de destino en la cual se hará la transferencia: 98765

Saldo de la cuenta: en Pesos Argentinos 85.000 (en Soles Peruanos 3.564)

Esta información se mantendrá constante (a excepción del saldo) durante la ejecución del
algoritmo.

# Grafos, Diagramas y complejidad ciclomatica de funciones 

### Funcion Seleccion de moneda:
![Image text](https://github.com/JuannHerna/Trabajo_final_cajero/blob/main/imagenes_de_diagramas/seleccion_moneda.jpg)
#### Complejidad ciclomatica
```
R= 2
V(G)= A - N + 2=8-8+2=2
V(G)= 1 + 1=2
```
#### Caminos posibles
#### Casos de pueba
#### Codigo de la funcion
``` python
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
```

### Funcion Cambio de moneda
![Image text](https://github.com/JuannHerna/Trabajo_final_cajero/blob/main/imagenes_de_diagramas/cambio_de_moneda.jpg)
#### Complejidad ciclomatica
```
R= 2
V(g)=A-N+2 = 7-7+2 = 2
V(g)=P+1 = 1+1 = 2
```
#### Caminos posibles
#### Casos de pueba
#### Codigo de la funcion
``` python
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
```
### Funcion Consultas
![Image text](https://github.com/JuannHerna/Trabajo_final_cajero/blob/main/imagenes_de_diagramas/consultas.jpg)

#### Complejidad ciclomatica
```
R= 5
V(g)= A -N +2 = 22 - 19 + 2 = 5
V(g)= P+1= 4 + 1 = 5
```
#### Caminos posibles
#### Casos de pueba

#### Codigo de Funcion
```python
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
```
### Funcion Retiros
![Image text](https://github.com/JuannHerna/Trabajo_final_cajero/blob/main/imagenes_de_diagramas/retiros.jpg)
#### Complejidad ciclomatica
```
R= 6
V(g)= A-N+2= 32 - 28 + 2 = 6
V(g)= 5 + 1 = 6
```
#### Codigo de funcion
``` python
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
```
