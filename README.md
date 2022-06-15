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
```
1) 1,2,3,4,5,6,7
2) 1,2,3,4,5,8,5,8,5,6,7
3)1,2,3,4,5,8,5,6,7
```
#### Casos de pueba
```
```
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
```
1) 1,2,3,4,5,6
2) 1,2,3,7,5,6
```
#### Casos de pueba
```
```
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
```
1) 1,2,3,4,5,6,7,9,10,11,12,19,20
2) 1,2,3,4,5,6,7,8,7,9,15,16,17,16,19,20
3)1,2,3,4,5,6,7,8,7,9,10,11,13,14,19,20
4)1,2,3,4,5,6,7,9,15,16,18,20
```
#### Casos de pueba
```
```

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
#### Caminos posibles
```
1) 1,2,3,4,5,6,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28
2) 1,2,3,4,7,8,9,10,14,26,27,28
3)1,2,3,4,7,8,9,10,11,12,13,14,26,27,28
4)1,2,3,4,5,6,10,11,12,13,14,26,27,28

```
#### Casos de pueba
```
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
### Funcion Transferencia
![Image text](https://github.com/JuannHerna/Trabajo_final_cajero/blob/main/imagenes_de_diagramas/transferencia.jpg)
#### Complejidad Cilomatica
```
R= 4
V(g)=27-25+2= 4
V(g)= 3+1= 4
```
#### Caminos posibles
```
```
#### Casos de pueba
```
```

#### Codigo de funcion
```python
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
```
### Funcion Validacion
![Image text](https://github.com/JuannHerna/Trabajo_final_cajero/blob/main/imagenes_de_diagramas/validacion.jpg)
#### Complejidad Cilomatica
```
R=6
V(g)= 31-27+2= 6
V(g)= P+1= 5+1= 6
```
#### Caminos posibles
```
```
#### Casos de pueba
```
```

#### Codigo de funcion
```python
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
```
### Funcion Principal
![Image text]()
#### Complejidad Cilomatica
```
R=5
V(g)= 18-15+2=5
V(g)= 4+1= 5
```
#### Caminos posibles
```
```
#### Casos de pueba
```
```

#### Codigo de funcion
```python
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
```
