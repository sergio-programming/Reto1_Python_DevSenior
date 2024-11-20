from datetime import datetime
import statistics
from textwrap import dedent

class Experimento:
    def __init__(self, nombre, fechaExperimento, tipoExperimento, resultadosObtenidos):
        self.nombre = nombre
        self.fechaExperimento = fechaExperimento
        self.tipoExperimento = tipoExperimento
        self.resultadosObetenidos = resultadosObtenidos
        
    
def ingresarExperimento(listaExperimentos):
    print()
    print("#"*30)
    print("MODULO DE REGISTRO DE EXPERIMENTOS")
    print("#"*30)
    try:
        nroExperimentos = int(input("\nDigite la cantidad de experimentos que desea ingresar: "))
    except ValueError:
        print("El dato de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
        return
        
    for i in range(nroExperimentos):
        nombre = input("\nPor favor ingrese el nombre del experimento: ")
        fechaExperimento_str = input("Por favor ingrese fecha de realización del experimento en el formato (DD/MM/AAAA): ")
        try:
            fechaExperimento = datetime.strptime(fechaExperimento_str, "%d/%m/%Y")
        except ValueError:
            print("\nLa fecha ingresada no es valida. Por favor intente de nuevo.")
            input("Presione <Enter> para continuar")
            return
            
        tipoExperimento = input("Ingrese el tipo de experimento (Ej: Quimica, Fisica, Biologia): ")
        resultadosObtenidos = []
        try:
            nroResultados = int(input("Por favor ingrese el numero de resultados que desea ingresar del experimento: "))
        except ValueError:
            print("El dato de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
            return
            
        for i in range(nroResultados):
            try:
                resultado = float(input(f"Ingrese el resultado #{i+1}: "))
            except ValueError:
                print("El dato de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")
                return
            resultadosObtenidos.append(resultado)
        
    experimento = Experimento(nombre, fechaExperimento, tipoExperimento, resultadosObtenidos)
    listaExperimentos.append(experimento)
        
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
            print(dedent(
                f"""\nExperimento #{i}:
                Nombre del experimento: {experimento.nombre}
                Fecha de realización: {experimento.fechaExperimento.strftime('%d/%m/%Y')}
                Tipo de Experimento: {experimento.tipoExperimento}
                Resultados Obtenidos: {experimento.resultadosObtenidos}"""
            ))
            
def analisisResultados(listaExperimentos):
    if not listaExperimentos:
        print("\nNo hay experimento ni resultados para visualizar.")
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
            print(dedent(
                f"""\nANALISIS DE RESULTADOS EXPERIMENTO: {experimento.nombre}
                Resultado Promedio: {promedio}
                Resultado Maximo: {maximo}
                Resultado Minimo: {minimo}"""
            ))
        
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
        print(dedent(
            """1. Registro de Experimentos.
            2. Visualizar experimentos.
            3. Analisis de Resultados.
            4. Generacion de Informe de Resultados.
            5. Salir del programa."""
            ))
        
        while True:
            try:
                opcion = int(input("Por favor ingrese una opcion: "))
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
            generarInforme(listaExperimentos)
    
        elif opcion == 5:
            print("\nGracias por usar nuestro software, nos vemos pronto!!!")
            input("Presione <Enter> para continuar")
            break
    
        else:
            print("\nLa opción ingresada no es valida. Por favor intente de nuevo.")
            input("Presione <Enter> para continuar")
                
                
if __name__ == "__main__":
    menu()