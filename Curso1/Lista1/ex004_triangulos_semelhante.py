class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def ordenar(self):
        return sorted([self.a, self.b, self.c])

    def semelhantes(self, triangulo):
        triangulo1 = list(self.ordenar())
        triangulo2 = list(triangulo.ordenar())
        return triangulo1[0] / triangulo2[0] == triangulo1[1] / triangulo2[1] and triangulo1[0] / triangulo2[0] == triangulo1[2] / triangulo2[2]
        
