from datetime import datetime
import statistics

#Clase Experimento con su constructor para inicializar los atributos
class Experimento:
    def __init__(self, nombre, fechaExperimento, tipoExperimento, resultadosObtenidos):
        self.nombre = nombre
        self.fechaExperimento = fechaExperimento
        self.tipoExperimento = tipoExperimento
        self.resultadosObtenidos = resultadosObtenidos
     
#Funcion para ingresar experimentos 
def ingresarExperimento(listaExperimentos):
    #Mensaje de bienvenida al modulo de registro de experimentos
    print()
    print("#"*30)
    print("MODULO DE REGISTRO DE EXPERIMENTOS")
    print("#"*30)
    #try-except para manejar errores por si el usuario no ingresa un número entero
    try:
        nroExperimentos = int(input("\nDigite la cantidad de experimentos que desea ingresar: "))
    #Si no se ingresa un número se captura el error y se muestra el mensaje    
    except ValueError:
        print("El tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
        return
    
    #Bucle for para que el usuario ingrese los datos de los experimentos    
    for i in range(nroExperimentos):
        nombre = input("\nPor favor ingrese el nombre del experimento: ")
        fechaExperimento_str = input("Por favor ingrese fecha de realización del experimento en el formato (DD/MM/AAAA): ")
        #try-except para manejar errores por si el usuario no ingresa la fecha en formato DD/MM/YYYY
        try:
            fechaExperimento = datetime.strptime(fechaExperimento_str, "%d/%m/%Y")
        #Si no se ingresa la fecha en el formato indicado se captura el error y se muestra el mensaje
        except ValueError:
            print("\nLa fecha ingresada no es valida. Por favor intente de nuevo.")
            input("Presione <Enter> para continuar")
            return
            
        tipoExperimento = input("Ingrese el tipo de experimento (Ej: Quimica, Fisica, Biologia): ")
        #Lista para almacenar los resultados ingresados por el usuario
        resultadosObtenidos = []
        #Bucle while para que solicite el dato hasta que se ingrese un numero mayor o igual a tres
        while True:
            #try-except para manejar errores por si el usuario no ingresa un número entero
            try:
                nroResultados = int(input("Por favor ingrese el numero de resultados que desea ingresar del experimento(Debes ingresar minimo 3): "))
                #Si el numero de resultados es mayor o igual a 3 el usuario podra ingresarlos
                if nroResultados >= 3:
                    #Bucle for para ingresar la cantidad de resultados indicada
                    for i in range(nroResultados):
                        while True:
                            try:
                                resultado = float(input(f"Ingrese el resultado #{i+1}: "))
                            except ValueError:
                                print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
                                input("Presione <Enter> para continuar")
                            else:
                                break                                                    
                        resultadosObtenidos.append(resultado)
                    break    
                else:
                    #Si el numero de resultados es menor a tres se mostrara el mensaje al usuario
                    print("\nNo se ingreso la cantidad minima de resultados para completar el proceso.")
                    input("Presione <Enter> para continuar")
            #Si no se ingresa un número se captura el error y se muestra el mensaje       
            except ValueError:
                print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")            
   
            
        #Se crea una instancia de la clase Experimento si todo esta correcta
        experimento = Experimento(nombre, fechaExperimento, tipoExperimento, resultadosObtenidos)
        #Se almacena cada experimento en la lista de experimentos
        listaExperimentos.append(experimento)   
    
    #Condicional para mostrar un mensaje de acuerdo a la cantidad de experimentos registrados    
    if nroExperimentos > 1:
        print("\nExperimentos agregados exitosamente!")
        input("Presione <Enter> para continuar")
    else:
        print("\nExperimento agregado exitosamente!")
        input("Presione <Enter> para continuar")

#Función para mostrar los experimentos        
def visualizarExperimentos(listaExperimentos):
    #Si no hay experimentos se mostrara un mensaje para indicarle al usuario
    if not listaExperimentos:
        print("\nNo hay experimentos para visualizar.")
        input("Presione <Enter> para continuar")
    #En caso contrario se muestran los experimentos en consola
    else:
        print()
        print("#"*30)
        print("MODULO DE VISTA DE EXPERIMENTOS")
        print("#"*30)
        #Bucle for para mostrar cada experimento
        for i, experimento in enumerate(listaExperimentos, start=1):
            print(
                f"""\nExperimento #{i}:
                Nombre del experimento: {experimento.nombre}
                Fecha de realización: {experimento.fechaExperimento.strftime('%d/%m/%Y')}
                Tipo de Experimento: {experimento.tipoExperimento}
                Resultados Obtenidos: {experimento.resultadosObtenidos}"""
            )

#Función para analizar los resultados de los experimentos            
def analisisResultados(listaExperimentos):
    #Si no hay experimentos se mostrara un mensaje para indicarle al usuario
    if not listaExperimentos:
        print("\nNo hay experimentos ni resultados para visualizar.")
        input("Presione <Enter> para continuar")
    #En caso contrario se muestran los analisis de los resultados en consola
    else:
        print()
        print("#"*30)
        print("MODULO DE ANALISIS DE EXPERIMENTOS")
        print("#"*30)       
        for experimento in listaExperimentos:
            promedio = statistics.mean(experimento.resultadosObtenidos)
            maximo = max(experimento.resultadosObtenidos)
            minimo = min(experimento.resultadosObtenidos)
            print(
                f"""\nANALISIS DE RESULTADOS EXPERIMENTO: {experimento.nombre}
                Resultado Promedio: {promedio}
                Resultado Maximo: {maximo}
                Resultado Minimo: {minimo}"""
            )

#Función para eliminar experimento            
def eliminarExperimento(listaExperimentos):
    #Si no hay experimentos se mostrara un mensaje para indicarle al usuario
    if not listaExperimentos:
        print("\nNo hay experimentos ni resultados para eliminar.")
        input("Presione <Enter> para continuar")
    #En caso contrario se solicita al usuario que indique el experimento que desea eliminar
    else:
        print()
        print("#"*30)
        print("MODULO DE ANALISIS DE EXPERIMENTOS")
        print("#"*30)
        #Bucle while para solicitar el dato hasta que se ingrese un número entero
        while True:
            #try-except para manejar errores por si el usuario no ingresa un número entero
            try:
                experimento_a_eliminar = int(input(f"\nElige un experimento a eliminar (Del 1 al {len(listaExperimentos)}): "))
            #Si no se ingresa un número se captura el error y se muestra el mensaje
            except ValueError:
                print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")
            else:
                break
        #Se elimina el elemento de la lista de experimentos
        listaExperimentos.pop(experimento_a_eliminar-1)
        print("\nExperimento eliminado exitosamente.")
        input("Presione <Enter> para continuar")
            
#Función para generar el informe en un archivo.txt     
def generarInforme(listaExperimentos):
    #Si no hay experimentos se mostrara un mensaje para indicarle al usuario
    if not listaExperimentos:
        print("\nNo hay experimentos registrados")
        input("Presione <Enter> para continuar")
    #En caso contrario se abrira y se empezara a escribir el informe    
    else:
        with open("informe_experimentos.txt", "w") as archivo:
            for experimento in listaExperimentos:
                archivo.write(f"Nombre: {experimento.nombre}\n")
                archivo.write(f"Fecha de realización: {experimento.fechaExperimento.strftime('%d/%m/%Y')}\n")
                archivo.write(f"Tipo de Experimento: {experimento.tipoExperimento}\n")
                archivo.write(f"Resultados Obtenidos: {experimento.resultadosObtenidos}\n")
                archivo.write("\n")
        print("Informe generado como 'informe_experimentos.txt")
        input("Presione <Enter> para continuar")
        

#Funcion para comparar experimentos
def compararExperimentos(listaExperimentos):
    #Si no hay experimentos se mostrara un mensaje para indicarle al usuario
    if not listaExperimentos:     
        print("\nNo hay experimentos ni resultados para eliminar.")
        input("Presione <Enter> para continuar")
        
    else:
        print()
        print("#"*30)
        print("MODULO DE COMPARATIVA DE EXPERIMENTOS")
        print("#"*30)
        print(f"\nActualmente tenemos {len(listaExperimentos)} registrados")
    
        while True:
            try:
                experimentos_a_comparar = int(input("\nPor favor ingrese cuantos experimentos desea comparar: "))
            except ValueError:
                print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")
            else:
                if experimentos_a_comparar < 2:
                    print("\nDebe seleccionar minimo 2 experimentos para comparar. Por favor intente")
                    input("Presione Enter para continuar")
                elif experimentos_a_comparar > len(listaExperimentos):
                    print("\nEstimado usuario, ud no puede comparar una cantidad de experimentos que es mayor a la cantidad de experimentos registrados. Por favor intente")
                    input("Presione Enter para continuar")
                else:
                    break
        
        experimentos = []
        promedios = []
        for i in range(experimentos_a_comparar):
            while True:
                try:
                    nroExperimento = int(input(f"Seleccione un experimento (ingrese un número del 1 al {len(listaExperimentos)}): "))
                    if nroExperimento < 1 or nroExperimento > len(listaExperimentos):
                        raise IndexError
                except ValueError:
                    print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
                    input("Presione <Enter> para continuar")
                except IndexError:
                    print("\nEl número ingresado esta fuera de rango. Por favor intente de nuevo.")
                    input("Presione <Enter> para continuar")
                else:
                    break
            experimentos.append(listaExperimentos[nroExperimento-1])
            promedio = statistics.mean(listaExperimentos[nroExperimento-1].resultadosObtenidos)
            promedios.append(promedio)
        
        print("\nResultados de los experimentos seleccionados:")    
        for i, experimento in enumerate(experimentos, start=0):
            print(f"""\nExperimento: {experimento.nombre}
Promedio de resultados del experimento: {promedios[i]}""")
            
        max_promedio = max(zip(promedios, experimentos), key=lambda x: x[0])
        print("\n" + "#"*30)
        print(f"\nEl experimento con el promedio mayor es: {max_promedio[1].nombre}")
        print(f"Promedio: {max_promedio[0]}")
        print("#"*30)
            
def menu():
    #Lista para almacenar los experimentos
    listaExperimentos = []
    #Bucle while para visualizar el menu hasta que se seleccione la opcion de salir
    while True:
        print()
        print("#"*30)
        print("BIENVENIDO A LA PLATAFORMA DE GESTION DE EXPERIMENTOS")        
        print("#"*30)
        print("""1. Registro de Experimentos.
2. Visualizar Experimentos.
3. Analisis de Resultados de Experimentos.
4. Eliminar Experimento.
5. Comparar Experimentos.
6. Generar Informe de Resultados.
7. Salir del programa.""")
            
        #Bucle while para solicitar la opcion hasta que se ingrese un número entero
        while True:
            try:
                opcion = int(input("\nPor favor ingrese una opcion: "))
            except ValueError:
                print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")
            else:
                break 
         
        #Condicionales para ejecutar cada una de las opciones del menu     
        if opcion == 1:
            ingresarExperimento(listaExperimentos)
    
        elif opcion == 2:
            visualizarExperimentos(listaExperimentos)
    
        elif opcion == 3:
            analisisResultados(listaExperimentos)
            
        elif opcion == 4:
            eliminarExperimento(listaExperimentos)
            
        elif opcion == 5:
            compararExperimentos(listaExperimentos)
    
        elif opcion == 6:
            generarInforme(listaExperimentos)
    
        elif opcion == 7:
            print("\nGracias por usar nuestro software, nos vemos pronto!!!")
            input("Presione <Enter> para continuar")
            break
    
        else:
            print("\nLa opción ingresada no es valida. Por favor intente de nuevo.")
            input("Presione <Enter> para continuar")
                
                
if __name__ == "__main__":
    menu()