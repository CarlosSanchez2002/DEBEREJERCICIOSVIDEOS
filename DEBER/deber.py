import os

while True:
    try:
        print("*"*10,"MENU DE EJERCICIOS DE VIDEOS PYTHON","*"*10)
        print("NOTA: Para terminar el programa digite 0")
        opcion = int(input("Ingrese el ejercicio que desea ejecutar (Entre 1-33): "))


        if opcion < 0 or opcion > 40:
            print("Solo se permiten numeros entre 1-33")
        elif opcion ==0:
            os.system("cls")
            print("Ha acabado el funcionamiento de este deber")
            break
        elif opcion ==1:
            os.system('cls')
            print("Hola Mundo")

        elif opcion ==2:
            os.system("cls")
            NOMBRE= "CARLOSSANCHEZ"
            print (NOMBRE)

            EDAD= 25
            print(EDAD)

            EDAD= True
            print(EDAD)

            SUELDO= 603.6
            print(SUELDO)

        elif opcion ==3:
            os.system("cls")
            nume1= "26"
            nume2= "43"
            print(nume1+nume2)


            num1= int(nume1)
            num2= int(nume2)
            print(num1+num2)


            sueldo= 12132.5
            sueldoentero= int(sueldo)
            print(sueldoentero)


            valor= "4500.64"
            valordecimal=float(valor)
            print(valordecimal*6)

            edad = 100
            print(len(str(edad)))

        elif opcion ==4:
            os.system("cls")
            ENTERO=54
            DECIMAL=23.04
            COMPLEJO = 45+5
            BOOLEANO= True
            print(ENTERO)
            print(DECIMAL)
            print(COMPLEJO)
            print(BOOLEANO)

            num1=45
            num2=8
            print("La suma es:",num1+num2)
            print("La resta es:",num1-num2)
            print("La multiplicacion es:",num1*num2)
            print("La division es:",num1/num2)
            print("La division exct. es:",num1//num2)
            print("La potencia es:",num1**num2)

        elif opcion ==5:
            os.system("cls")
            TEXTO1 = "hola"
            TEXTO2 = "mundo"
            textofin = TEXTO1 + " " + TEXTO2
            print(textofin)

            print("El saludo es: %s %s" % (TEXTO1, TEXTO2))

            saludofin = "Saludo: {0} {1}".format(TEXTO1, TEXTO2)
            print(saludofin)

            saludofin2 = "Saludo: {y} {x}".format(x=TEXTO2, y=TEXTO1)
            print(saludofin2)
        elif opcion ==6:
            os.system("cls")   
            textocs = "wenas tardes binvenidos a la tarea de carlos sanchez"

            print(textocs)
            print(textocs.lower())
            print(textocs.upper())
            print(textocs.title())
            print(textocs.find("rd")) #Devuelve la posicion 
            print(textocs.count("o")) #Devuelve la cantidad de o

            textofin = textocs.replace("e", "3")
            print(textofin)

            valor = textocs.isnumeric()
            print(valor)

            cadenasep = textocs.split(" ") #separa en una lista las palabras
            print(cadenasep)


        elif opcion ==7:
            os.system("cls") 
            tupla = (4, 9, 6)
            print(tupla)
            tupla2 = (5, "carlos", True, 456.4, 45 + 7j, 98, "fresco", False)
            print(tupla2)
            tupla3 = (8, 4, (2, 4, 7))
            print(tupla3)
            print(tupla2[1])
            print(tupla2[-1])
            print(tupla2[0:4])
            print(tupla2[-2])

            a, b, c = tupla
            print(a)
            print(b)
            print(c)

            tuplafin = tupla + tupla3
            print(tuplafin)

            print(tuplafin.count(7)) #Sirve para contar cuantos 4 existen en la tupla
            print(tuplafin.index(8)) #Devuielve la posicion en donde se situa este numero


        elif opcion ==8:
            os.system("cls")
            LISTA1 = ["carlos", 57, 78.6, True, "joel", 98.1]
            print(LISTA1)
            print(LISTA1[:])
            print(LISTA1[2])
            print(LISTA1[-1])

            print(LISTA1[0:3])
            print(LISTA1[:2])
            print(LISTA1[3:])

            LISTA1.append("merzian") # añadir elemento al final
            print(LISTA1)

            LISTA1.insert(4, "guayakill") #añadir elemento en una posicion especifica
            print(LISTA1)

            LISTA1.extend(["pepe", 564, False]) #añadir otra lista
            print(LISTA1)

            print(LISTA1.index("joel")) #devuelve la posicion 

            LISTA1.remove(98.1) #busca y quita el valor
            print(LISTA1)

            LISTA1.pop() #elimina el ultimo valor
            print(LISTA1)

            LISTA2 = ["duran", "melany"]
            LISTA3 = LISTA1 + LISTA2
            print(LISTA3)

            print(LISTA2 * 4)

            print("joel" in LISTA1)


        elif opcion ==9: #clave:valor
            os.system("cls")    
            DICCsUNEMI = {"Ecuador": "Guayakill", "Argentina": "Buenos Aires", "Chile": "Santiago de Chile"}
            print(DICCsUNEMI["Argentina"])
            print(DICCsUNEMI)

            DICCsUNEMI["Peru"] = "Lima" #para agregar
            print(DICCsUNEMI)

            DICCsUNEMI["Ecuador"] = "Quito"
            print(DICCsUNEMI)

            del DICCsUNEMI["Ecuador"] #delete
            print(DICCsUNEMI)

            DICS2 = {"Sanchez": "Carlos", 25: True, "Sueldo": 465.65}
            print(DICS2[25])

            LLAVES = ("Ecuador", "Italia", "Francia")
            DICSPAIS = {LLAVES[0]: "Guayakill", LLAVES[1]: "Roma", LLAVES[2]: "Paris"}
            print(DICSPAIS)

            MISDATOS = {"Apellido": "Sanchez", "Tiempo": {1: 2009, 2: 2010, 3: 2011, 4: 2012, 5: 2013}}
            print(MISDATOS)
            print(MISDATOS["Tiempo"])

            print(MISDATOS.get('lido', "Carlos")) #busca la clave y presena su valor, de no encontrarla devuelve el valor introducido

            print(MISDATOS.keys()) #retorna solo las llaves
            VALORS = tuple(MISDATOS.values()) #retorna solo los valores
            print(VALORS)


        elif opcion ==10:

            os.system("cls")
            NOMBRE = input("Ingrese su nombre: ")
            EDAD = int(input("Ingrese su edad: "))
            SUELDO = float(input("Ingrese su sueldo: "))

            print("Hola, " + NOMBRE)
            EDADFUT = EDAD + 20
            print("Tu edad es:", EDAD)
            print("Tu edad (dentro de 20 años) será:", EDADFUT)
            print("Tu sueldo es:", SUELDO)


        elif opcion ==11:
            os.system("cls")
            EDAD = int(input("Ingrese su edad: "))

            if EDAD > 21:
                print("Puedes entrar a la discoteca.")
            elif EDAD == 21:
                print("Tienes 21 años")
            else:
                print("No puedes entrar a la discoteca.")


        elif opcion ==12:
            os.system("cls")
            def saludo():
                print("Sanchez")
                print("Carlos")
                print("Merzian")
                return "Buenas tardes"

            print(saludo())

            def evaluarsueldo(sueldo):
                if sueldo >= 350:
                    print("Tienes buen sueldo")
                else:
                    print("Eres tremendo pobre")

            evaluarsueldo(200)
        elif opcion ==13:
            os.system("cls")
            DISTANCIA = 822
            NUMHERM = 9
            SALARIOP = 1000

            BENEFICIO = False

            if (DISTANCIA > 1000 and NUMHERM > 4) or SALARIOP < 2000: #F
                BENEFICIO = True

            print(not BENEFICIO)

            if (9 > 70) or (8 < 4):
                print("Verdadero")
            else:
                print("Es falso")


        elif opcion ==14:
            os.system("cls")
            SEXOS = ("Femenino", "Masculino")
            POSICION = True
            SEXO = SEXOS[POSICION] #M
            print(SEXO)
            SEXO = SEXOS[not POSICION] #F
            print(SEXO)


        elif opcion ==15:
            os.system("cls")    
            NUMEROS = range(15)
            print(NUMEROS[6])

            NUMEROS1 = range(8, 65)
            print(NUMEROS1[9])

            NUMEROS2 = range(45, 526565, 9)
            print(NUMEROS2[15])


        elif opcion ==16:
            os.system("cls")
            for Z in range(6, 45):
                print("{0} x {1} es: {2}".format(Z, Z, (Z * Z)))

            for NOMBRES in ["Melany", "Carlos", "Pepe", "Daniel"]:
                print("Cantidad de letras de {0} es: {1}".format(NOMBRES, len(NOMBRES)))


        elif opcion ==17:
            os.system("cls")
            print("-- MATERIAS --")
            print("Fisica - Quimica - Historia - Ingles")

            materia = input("Ingrese la materia deseada: ")
            materia1=materia.title()

            if materia1 in ("Fisica", "Quimica", "Historia", "Ingles"):
                print("Materia {0} seleccionada.".format(materia1))
            else:
                print("No existe esa materia")


        elif opcion ==18:
            os.system("cls")   
            NUMERO = int(input("Ingrese un número: "))
            FACT = 1
            for n in range(1, (NUMERO + 1)):
                FACT = FACT * n

            print("El factorial de {0} es: {1}".format(NUMERO, FACT)) 


        elif opcion ==19:
            os.system("cls")
            INICIO = 8

            while INICIO <= 500:
                print("Numero par: {0}".format(INICIO))
                INICIO += 2

            print("ACABO EL BUCLE .")


        elif opcion ==20:
            os.system("cls")
            for NUM in range(6, 20):
                if NUM <= 9:
                    pass
                else:
                    print("El siguiente numero es mayor a 9:")
                print("El num es: {0}".format(NUM))

            print("Se termino.")

            def funciondemas():
                pass


        elif opcion ==21:
            os.system("cls")    
            def generadormult7(limite):
                NUM = 4

                while NUM <= limite:
                    yield NUM * 9 #yiel genera un objeto iterable,que peude recorrer
                    NUM = NUM + 1


            obtienemul7 = generadormult7(10)

            print(next(obtienemul7))
            print(" hay 300 líneas de codigo")
            print(next(obtienemul7))
            print(" hay 1000 líneas de codigo")
            print(next(obtienemul7))


        elif opcion ==22:
            os.system("cls")
            def devolverlen(*lenguajes): #recibir una cantidad indeterminada de parametros
                for letra in lenguajes:
                    yield from letra

            lenguajes = devolverlen("Python", "Java", "CSS", "Ruby", "Javascript")

            print(next(lenguajes))
            print(next(lenguajes))
            print(next(lenguajes))
            print(next(lenguajes))
            print(next(lenguajes))



        elif opcion ==23: #Ejercicio de saltar error a proposito con try
            os.system("cls")
            NUM1 = 64
            NUM2 = 6
            try:
                R = NUM1 / NUM2
            except ZeroDivisionError:
                print("No se divide entre 0 ")
            finally:
                print("Aqui ando")
            print("Aqui acaba mi archivo.")
            

        elif opcion ==24: #Ejercicio para crear execpciones personalizadas
            os.system("cls")   
            def evaluarNota(nota):
                if nota < 0:
                    raise ValueError("Valor incorrecto")
                elif nota >= 16:
                    print("Pasaste")
                elif nota >= 11:
                    print("Raspaste")
                else:
                    print("Te quedaste")

            evaluarNota(7)

            print("Aqui termina")

        elif opcion ==25:
            os.system("cls")
            from modulos.EJ25 import *

            print(sumar(6, 9))
            print(multiplicar(5, 8))


        elif opcion ==26:
            os.system("cls")
            from paquete1.EJ27 import contar_letras
            from paquete1.EJ28 import *

            print(multiplicar(8,9))
            print(contar_letras("carlosjoelsanchezgalan"))


        elif opcion ==27:
            os.system("cls")
            class Persona():
                APELLIDOS = ""
                NOMBRES = ""
                EDAD = 0
                DESPERTAR = False

                def despertar(self):
                    self.DESPERTAR = True
                    print("Wenos dias")


            PERSONA1 = Persona()
            PERSONA1.APELLIDOS = "SANCHEZ GALAN"
            print(PERSONA1.APELLIDOS)
            PERSONA1.despertar()
            print(PERSONA1.DESPERTAR)

            PERSONA2 = Persona()
            PERSONA2.APELLIDOS = "CHARY SANCHEZ"
            print(PERSONA2.APELLIDOS) #no llamamos a la funcion despertar y el print dira false 
            print(PERSONA2.DESPERTAR)


        elif opcion ==28:
            os.system("cls")


            class Curso():
                def __init__(self, nom, cre, pro):
                    self.NOMBRE = nom
                    self.CREDITOS = cre
                    self.PROF = pro
                    self.__imparticion = "Presencial" #agregar __ hace que la propiedad esté encapsulada, es decir que no puede ser accedida desde fuera

                def mostrarDatos(self):
                    dat = "Nombre: {} / Créditos: {} / Modalidad: {}"
                    print(dat.format(self.NOMBRE, self.CREDITOS, self.__imparticion))

                    DOCEASIG = self.__verificarDocente()
                    if DOCEASIG:
                        print("Existe docente")
                    else:
                        print("No es necesario dar un docente")

                def __verificarDocente(self):
                    if self.__imparticion == "Presencial":
                        return True
                    else:
                        return False

            curso1 = Curso("Fisica", 7, "Ingeniería IND.")
            curso1.mostrarDatos()



        elif opcion ==29:
            os.system("cls")


            class Cuenta():

                def __init__(self, pro, sal, mon):
                    self.__PROPIE = pro
                    self.__SALDO = sal
                    self.__MONEDA = mon

                def get_Saldo(self):  #Para obtener propiedades encapsuladas
                    return self.__SALDO

                def get_Propietario(self):
                    return self.__PROPIE

                def get_Moneda(self):
                    return self.__MONEDA

                def set_Moneda(self, MONEDA): #set para modificar en este caso moneda 
                    self.__MONEDA = MONEDA


            CTA1 = Cuenta("CARLOS SANCHEZ", 65000, "PESOS")
            print(CTA1.get_Saldo())
            print(CTA1.get_Moneda())
            CTA1.set_Moneda("EUROS")
            print(CTA1.get_Moneda())


        elif opcion ==30:
            os.system("cls")


            class Persona():

                def __init__(self, apePat, apeMat, nom):
                    self.apellidopadre = apePat
                    self.apellidomadre = apeMat
                    self.nombres = nom

                def nombrecompleto(self):
                    txt = "{} {}, {}"
                    return txt.format(self.apellidopadre, self.apellidomadre, self.nombres)

                def datos(self):
                    print(self.nombrecompleto())


            class Estudiante(Persona):

                def __init__(self, apePat, apeMat, nom, pro):
                    super().__init__(apePat, apeMat, nom) #super hace que herede de la clase persona los parametros
                    self.profesion = pro

                def datos(self):
                    super().datos()
                    print("Profesión: {}".format(self.profesion))


            per1 = Persona("Sanchez", "Galan", "Carlos")
            print(isinstance(per1, Estudiante)) #isinstance sirve para verificar si una instancia pertenece a una


        elif opcion ==31: #herencia multiple
            os.system("cls")


            class Clase1():

                def __init__(self, par1, par2):
                    self.PARAMETRO1 = par1
                    self.PARAMETRO2 = par2


            class Clase2():

                def __init__(self, par3, par4, par5):
                    self.PARAMETRO3 = par3
                    self.PARAMETRO4 = par4
                    self.PARAMETRO5 = par5


            class ClaseX(Clase1, Clase2):
                pass


            cX1 = ClaseX(15, 21)


        elif opcion ==32: # polimorfismo. Llamar a las clases y usar sus metodos
            os.system("cls")


            class Estudiante():

                def describir(self):
                    print("Soy pilas para estudiar")


            class Docente():

                def describir(self):
                    print("Enseño Frances")


            class Trabajador():

                def describir(self):
                    print("Trabajo en una  empresa.")


            def describirper(persona):
                persona.describir()


            doc1 = Estudiante()
            describirper(doc1)


        elif opcion ==33:
            os.system("cls")


            class Pais():
                def __init__(self, nom, pre):
                    self.NOMBRE = nom
                    self.PRESI = pre

                def __str__(self): #metodo string 
                    txt = "País: {} - Presidente: {}"
                    return txt.format(self.NOMBRE, self.PRESI)


            class Ciudad():
                def __init__(self, nom, hab, pai):
                    self.NOMBRE = nom
                    self.habitantes = hab
                    self.PAIS = pai

                def __str__(self):
                    txt = "Ciudad: {} - N° Habitantes: {} ({})"
                    return txt.format(self.NOMBRE, self.habitantes, self.PAIS)


            class Urbanizacion():
                def __init__(self, nom, ciu):
                    self.NOMBRE = nom
                    self.CIUDAD = ciu

                def __str__(self):
                    txt = "Urbanización: {} ({})"
                    return txt.format(self.NOMBRE, self.CIUDAD)


            PAIS1 = Pais("Ecuador", "Guillermo Lasso")
            print(PAIS1)

            CIUDAD1 = Ciudad("Guayakill", 50000000, PAIS1) #va a mostrar los parametros actuales + parametros de PAIS1
            print(CIUDAD1)

            URB1 = Urbanizacion("Ciudad Celeste", CIUDAD1)#va a mostrar los parametros actuales + parametros de CIUDAD1 +PAIS1
            print(URB1)

    except ValueError:
        os.system("cls")
        print("Los caracteres no estan permitidos en este ejercicio")
