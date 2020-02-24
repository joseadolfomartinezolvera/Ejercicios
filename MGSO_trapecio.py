class OpeTrap:
    def area_trapecio(self):
        B=int(input('Ingrese la base 1: '))
        b=int(input('Ingrese la base 2: '))
        h=int(input('Ingrese la altura: '))

        print((B+b)*h/2)

trapecio= OpeTrap()
trapecio.area_trapecio()
