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
    except ValueError:
        print("El dato de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
        return
    
    #Bucle for para que el usuario ingrese la cantidad de experimentos deseada    
    for i in range(nroExperimentos):
        nombre = input("\nPor favor ingrese el nombre del experimento: ")
        fechaExperimento_str = input("Por favor ingrese fecha de realización del experimento en el formato (DD/MM/AAAA): ")
        #try-except para manejar errores por si el usuario no ingresa la fecha en formato DD/MM/YYYY
        try:
            fechaExperimento = datetime.strptime(fechaExperimento_str, "%d/%m/%Y")
        except ValueError:
            print("\nLa fecha ingresada no es valida. Por favor intente de nuevo.")
            input("Presione <Enter> para continuar")
            return
            
        tipoExperimento = input("Ingrese el tipo de experimento (Ej: Quimica, Fisica, Biologia): ")
        #Lista para almacenar los resultados ingresados por el usuario
        resultadosObtenidos = []
        
        while True:
            #try-except para manejar errores por si el usuario no ingresa un número entero
            try:
                nroResultados = int(input("Por favor ingrese el numero de resultados que desea ingresar del experimento(Debes ingresar minimo 3): "))
                if nroResultados >= 3:
                    for i in range(nroResultados):
                        while True:
                            try:
                                resultado = float(input(f"Ingrese el resultado #{i+1}: "))
                            except ValueError:
                                print("\nEl dato de dato ingresado no es valido. Por favor ingrese un número.")
                                input("Presione <Enter> para continuar")
                            else:
                                break                                                    
                        resultadosObtenidos.append(resultado)
                    break    
                else:
                    print("\nNo se ingreso la cantidad minima de resultados para completar el proceso.")
                    input("Presione <Enter> para continuar")
            except ValueError:
                print("\nEl dato de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")            
   
            
        
        experimento = Experimento(nombre, fechaExperimento, tipoExperimento, resultadosObtenidos)
        listaExperimentos.append(experimento)   
    
    #Condicional para mostrar un mensaje de acuerdo a la cantidad de experimentos registrados    
    if nroExperimentos > 1:
        print("\nExperimentos agregados exitosamente!")
        input("Presione <Enter> para continuar")
    else:
        print("\nExperimento agregado exitosamente!")
        input("Presione <Enter> para continuar")
        
def visualizarExperimentos(listaExperimentos):
    if not listaExperimentos:
        print("\nNo hay experimentos para visualizar.")
        input("Presione <Enter> para continuar")
    else:
        print()
        print("#"*30)
        print("MODULO DE VISTA DE EXPERIMENTOS")
        print("#"*30)
        for i, experimento in enumerate(listaExperimentos, start=1):
            print(
                f"""\nExperimento #{i}:
                Nombre del experimento: {experimento.nombre}
                Fecha de realización: {experimento.fechaExperimento.strftime('%d/%m/%Y')}
                Tipo de Experimento: {experimento.tipoExperimento}
                Resultados Obtenidos: {experimento.resultadosObtenidos}"""
            )
            
def analisisResultados(listaExperimentos):
    if not listaExperimentos:
        print("\nNo hay experimentos ni resultados para visualizar.")
        input("Presione <Enter> para continuar")
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
            
def eliminarExperimento(listaExperimentos):
    if not listaExperimentos:
        print("\nNo hay experimentos ni resultados para visualizar.")
        input("Presione <Enter> para continuar")
    else:
        print()
        print("#"*30)
        print("MODULO DE ANALISIS DE EXPERIMENTOS")
        print("#"*30)
        while True:
            try:
                experimento_a_eliminar = int(input(f"\nElige un experimento a eliminar (Del 1 al {len(listaExperimentos)}): "))
            except ValueError:
                print("\nEl dato de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")
            else:
                break
        listaExperimentos.pop(experimento_a_eliminar-1)
        print("\nExperimento eliminado exitosamente.")
        input("Presione <Enter> para continuar")
            
        
def generarInforme(listaExperimentos):
    if not listaExperimentos:
        print("\nNo hay experimentos registrados")
        input("Presione <Enter> para continuar")
    else:
        with open("informe_experimentos.txt", "w") as archivo:
            for experimento in listaExperimentos:
                archivo.write(f"Nombre: {experimento.nombre}\n")
                archivo.write(f"Fecha limite: {experimento.fechaExperimento.strftime('%d/%m/%Y')}")
                archivo.write(f"Categoria: {experimento.tipoExperimento}\n")
                archivo.write(f"Horas dedicadas: {experimento.resultadosObtenidos}\n")
                archivo.write("\n")
        print("Informe generado como 'informe_experimentos.txt")
    
        
            
def menu():
    listaExperimentos = []
    while True:
        print()
        print("#"*30)
        print("BIENVENIDO A LA PLATAFORMA DE GESTION DE EXPERIMENTOS")        
        print("#"*30)
        print("""1. Registro de Experimentos.
2. Visualizar Experimentos.
3. Analisis de Resultados de Experimentos.
4. Eliminar Experimento.
5. Generacion de Informe de Resultados.
6. Salir del programa.""")
            
        
        while True:
            try:
                opcion = int(input("\nPor favor ingrese una opcion: "))
            except ValueError:
                print("\nEl dato de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")
            else:
                break 
            
        if opcion == 1:
            ingresarExperimento(listaExperimentos)
    
        elif opcion == 2:
            visualizarExperimentos(listaExperimentos)
    
        elif opcion == 3:
            analisisResultados(listaExperimentos)
            
        elif opcion == 4:
            eliminarExperimento(listaExperimentos)
    
        elif opcion == 5:
            generarInforme(listaExperimentos)
    
        elif opcion == 6:
            print("\nGracias por usar nuestro software, nos vemos pronto!!!")
            input("Presione <Enter> para continuar")
            break
    
        else:
            print("\nLa opción ingresada no es valida. Por favor intente de nuevo.")
            input("Presione <Enter> para continuar")
                
                
if __name__ == "__main__":
    menu()