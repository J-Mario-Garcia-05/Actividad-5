class Estudiante:
    def __init__(self, nombre, carne, carrera, nota_final):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.__nota_final = nota_final
    @property
    def nota_final(self):
        return self.__nota_final
    @nota_final.setter
    def nota_final(self, value):
        if 0 <= value <= 100:
            self.__nota_final = value
        else:
            raise ValueError("Error: la nota que ingreso no es válida")
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, carne: {self.carne}, carrera: {self.carrera}, nota final: {self.nota_final}")

lista_estudiantes = []
numero_carne = 10001
opcion  = "0"
while opcion != "5":
    print("\t==MENÚ==")
    print("1.Registrar estudiante")
    print("2.Mostrar estudiantes registrados")
    print("3.Buscar estudiante")
    print("4.Calcular promedio de notas de estudiantes")
    print("5.Salir")
    try:
        opcion = input("\nSeleccione una opción: ")
        match opcion:
            case "1":
                print("Ingrese los datos del estudiante:")
                nombre = input("Nombre: ")
                carrera = input("Carrera: ")
                nota_final = int(input("Nota final: "))
                registrar_estudiante = Estudiante(nombre, numero_carne, carrera, nota_final)
                lista_estudiantes.append(registrar_estudiante)
                print(f"El registro se completo con exito, número de carné asignado {numero_carne}.")
                numero_carne += 1
            case "2":
                if lista_estudiantes:
                    print("Estudiantes registrados:")
                    for estudiante in lista_estudiantes:
                        estudiante.mostrar_informacion()
                else:
                    print("No hay estudiantes registrados")
            case "3":
                if lista_estudiantes:
                    carne = int(input("Ingrese el Carné del estudiante que desea buscar: "))
                    for estudiante in lista_estudiantes:
                        if estudiante.carne == carne:
                            estudiante.mostrar_informacion()
                            carne = -1
                    if carne != -1:
                        print("No hay ningún estudiante con el número de carné.")
                else:
                    print("No hay estudiantes registrados")
            case "4":
                if lista_estudiantes:
                    sumar = 0
                    for estudiante in lista_estudiantes:
                        sumar += estudiante.nota_final
                    print(f"Promedio de notas de estudiantes: {sumar /len(lista_estudiantes)}")
                else:
                    print("No hay estudiantes registrados")
            case "5":
                print("Saliendo, que tenga buen día.")
            case __:
                print(f"La opción {opcion} no está disponible.")
        if opcion != "5":
            input("Presione ENTER para continuar: ")
    except Exception as e:
        print("ERROR: "+ str(e))