import sys #importa system para leer desde terminal

'''
    Comprueba que las cadenas solo tengan unos
        -revisa caracter por caracter
        -regresa false si la cadena contiene algo diferente a unos
        -Regresa True si contiene puros unos
'''
def comprobarCadena(cadena):
    for i in cadena:
        if i!='1':
            return False
    return True

'''
    funcion resta: contiene el algoritmo para restar
        -recibe 2 cadenas
        -las concatena con una "b" al inicio y al final y un "-" enmedio
        -Ejecuta el algoritmo de resta
            +Recorrer los '1' del primer numero hasta encontrar el '-'
            +Regresarse al '1' anterior y cambiarlo por '-' (ahora hay 2 '-')
            +Avanzar al '-' siguiente y cambiarlos por '1'
            +Recorrer todos los '1' hast ala primera 'b'
            +Borrar los dos '1' anteriores a la 'b'
            +Regresar hasta el inicio de la cinta
            +Repetir hasta que no haya '1' antes o despues del '-'
            +Si se terminan los '1' antes del '-', convertirlo en 'b'
        -Regresa la lista llamada cinta
'''
def restar(cad1, cad2):
    q0,q1,q2,q3,q4,q5,i=1,0,0,0,0,0,1
    #Concatenar Cadenas y convertirla en una lista para simular cinta
    cad1='b'+cad1+'-'+cad2+'b'
    cinta=list(cad1)
    #Algoritmo para restar
    while True:
        #Accoines en el estado q0
        if (q0==1):
            #(q0,1)=(q0,1,R)
            if cinta[i]=='1':
                i+=1
            #(q0,-)=(q1,1,L)
            elif cinta[i]=='-':
                i-=1
                q0,q1=q1,q0
            #(q0,b)=(q2,b,L)
            else:
                i-=1
                q0,q2=q2,q0
        #Accoines en el estado q1
        elif (q1==1):
            #(q1,1)=(q1,-,R)
            if cinta[i]=='1':
                cinta[i]='-'
                i+=1
            #(q1,-)=(q0,1,S)
            elif cinta[i]=='-':
                cinta[i]='1'
                q0,q1=q1,q0
            #(q1,b)=(h,b,S)
            else:
                cinta[i]='b'
                return cinta
        #Acciones en el estado q2
        elif (q2==1):
            #(q2,1)=(q3,b,L)
            if cinta[i]=='1':
                cinta[i]='b'
                i-=1
                q2,q3=q3,q2
        #Acciones en el estado q3
        elif (q3==1):
            #(q3,1)=(q4,b,L)
            if cinta[i]=='1':
                cinta[i]='b'
                i-=1
                q3,q4=q4,q3
        #Accoines en el estado q4
        elif (q4==1):
            #(q4,1)=(q1,1,S)
            if cinta[i]=='1':
                q4,q5=q5,q4
            #(q4,-)=(h,b,S)
            elif cinta[i]=='-':
                cinta[i]='b'
                return cinta
        #Accoines en el estado q5
        elif (q5==1):
            #(q5,1)=(q5,1,L) or (q5,-)=(q5,-,L)
            if cinta[i]=='1' or cinta[i]=='-':
                i-=1
            #(q5,b)=(q0,b,R)
            else:
                i+=1
                q5,q0=q0,q5

'''
    funcion main:
        -Comprueba las cadenas
        -Ejecuta funcion con el algoritmo para restar
        -Imprime el resutlado
'''
def main():
    if(not comprobarCadena(sys.argv[1])):
        sys.exit("Error cadena 1")
    if(not comprobarCadena(sys.argv[2])):
        sys.exit("Error cadena 2")
    print(restar(sys.argv[1], sys.argv[2]))

#le indica a python que existe un main
if __name__ == '__main__':
    main()
