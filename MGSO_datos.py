def datos():
    nombre = input('Ingrese su nombre: ')
    edad = input('Ingrese su edad: ')
    correo = input('Ingrese su direccion de correo electrónico: ')
    telefono = input('Ingrese su número de telefono ')
    persona = {'nombre': nombre, 'edad': edad, 'correo': correo, 'telefono': telefono}
    print(persona['nombre'], 'tiene', persona['edad'], 'años, su correo electrónico es ', persona['correo'], 'y su número de teléfono es', persona['telefono'])
    
datosPersona= datos()

