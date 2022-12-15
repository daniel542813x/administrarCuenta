class Usuario:
  # Método constructor
  def __init__(self, nombre, apellido, cedula, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.cedula = cedula
    self.edad = edad

# Clase Cuenta
class Cuenta(Usuario):
  # Método constructor
  def __init__(self, nombre, apellido, cedula, edad, saldo):
    super().__init__(nombre, apellido, cedula, edad)
    self.saldo = saldo

  # Método set para actualizar el saldo
  def setSaldo(self, saldo):
    self.saldo = saldo

  # Método get para obtener el saldo
  def getSaldo(self):
    return self.saldo

  # Método para mostrar un resumen del cliente y su saldo
  def mostrar(self):
    print("Datos del cliente:")
    print("Nombre:", self.nombre)
    print("Apellido:", self.apellido)
    print("Cédula:", self.cedula)
    print("Edad:", self.edad)
    print("Saldo:", self.saldo)

  # Método para simular una consignación de dinero
  def ingresar(self, cantidad):
    if cantidad > 0:
      self.saldo += cantidad
      print("La consignación se realizó con éxito")
    else:
      print("La cantidad a consignar debe ser mayor que cero")

  # Método para disminuir una cantidad de dinero en la cuenta
  def retirar(self, cantidad):
    if cantidad > 0:
      if self.saldo >= cantidad:
        self.saldo -= cantidad
        print("El retiro se realizó con éxito")
      else:
        print("No hay suficiente saldo en la cuenta")
    else:
      print("La cantidad a retirar debe ser mayor que cero")

# Clase Beneficio
class Beneficio(Cuenta):
  # Método constructor
  def __init__(self, nombre, apellido, cedula, edad, saldo):
    super().__init__(nombre, apellido, cedula, edad, saldo)

  # Método para validar si el usuario es mayor de edad pero menor de 28 años
  def usuarioValido(self):
    if self.edad > 17 and self.edad < 28:
      return True
    else:
      return False

  # Método para mostrar el total más el interés del 5%
  def mostrar(self):
    super().mostrar()
    if self.usuarioValido():
      interes = self.saldo * 0.05
      total = self.saldo + interes
      print("El interés generado es de:", interes)
      print("El total con el interés incluido es de:", total)
    else:
      print("Este usuario no tiene derecho a beneficios por ser mayor de edad")
