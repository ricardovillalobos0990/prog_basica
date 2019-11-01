class Usuario():
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.__password = self.__generar_password(password)

    
    def __generar_password(self, password):
        return password.upper()

    def get_password(self):
        return self.__password

ricardo = Usuario("ricardo", "villalobos@", "Osama1234" )

print(ricardo.nombre)
print(ricardo.email)
print(ricardo.get_password())
#print(ricardo.password)