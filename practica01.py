#Libreria para el tiempo
import time

def IngresarDatos():
    n=int(input('\n   Defina el tamaño del arreglo: '))
    N=[0]*n
    for i in range(n):
        num=int(input(f'   Ingrese el número en la posicion {i}: '))
        N[i]=num
    print('\n   Arreglo Original:')
    print('   ',N)
    #Indicamos cual es el valor que nosotros returnaremos de esta funcion
    return N

def Mostrar(N):
    print('\n   Arreglo Ordenado:')
    #Indicamos cual es el valor que nosotros returnaremos de esta funcion
    print('   ',N)
    
def Burbuja(N):
    L=len(N)
    #Dara el recorrido de las comparaciones
    for i in range (0,L):
        #Hara las comparaciones de los números
        for j in range (0,L-1):
            #Hacemos las comparaciones
            if N[j]>N[j+1]:
                #Guardamos el valor de la posicion j+1
                AUX=N[j]
                #Cambiamos de lugar el numero en la poisicion j
                N[j]=N[j+1]
                #Guardamos el siguiente valor que cambiaremos
                N[j+1]=AUX
    #Indicamos cual es el valor que nosotros returnaremos de esta funcion
    return N
    
def BurbujaOptimizada(N):
    L=len(N)
    #Esta variable revisara cuando ya se han hecho comparaciones
    C=False
    T=L
    for i in range (0,L):
        if C==True:
            break
        for j in range (0,T-1):
            C==True
            if N[j]>N[j+1]:
                C==False
                AUX=N[j]
                N[j]=N[j+1]
                N[j+1]=AUX
        T=T-1
    return N

opc=0
while opc!=3:
    print('\n    Menu')
    print('''
    1. Burbuja
    2. Burbuja Optimizada
    3. SALIR''')
    print('\nSeleccione una Opcion: ') 
    opc=int(input())
    if opc==1:
        inicio=time.time()
        print('\n-> Burbuja')
        #Igualamos nuestras funciones al arreglo que usaremos
        N=IngresarDatos()
        #Nuestro arreglo sera igual al nuevo arreglo que nos returne la funcion
        N=Burbuja(N)
        #Mandamos llamar nuestra funcion que mostrara los datos ya ordenados
        Mostrar(N)
        fin = time.time()
        tiempo_ejecutado = fin - inicio
        print('\n   Tiempo de ejecucion: ',tiempo_ejecutado)
    if opc==2:
        inicio=time.time()
        print('\n-> Burbuja Optimizada')
        #Igualamos nuestras funciones al arreglo que usaremos
        N=IngresarDatos()
        #Nuestro arreglo sera igual al nuevo arreglo que nos returne la funcion
        N=BurbujaOptimizada(N)
        #Mandamos llamar nuestra funcion que mostrara los datos ya ordenados
        Mostrar(N)
        fin = time.time()
        tiempo_ejecutado = fin - inicio
        print('\n   Tiempo de ejecucion: ',tiempo_ejecutado)
    if opc==3:
        print('\nEl programa ha terminado')