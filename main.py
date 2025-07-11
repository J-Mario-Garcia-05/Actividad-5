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
