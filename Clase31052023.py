class Personaje:
    #Constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        #Atributos
        self.name=nombre
        self.strength=fuerza
        self.intelligence=inteligencia
        self.defense=defensa
        self.life=vida

    #Metodos
    def atributos(self):
        print("Nombre: ", self.name)
        print("Fuerza: ",self.strength)
        print("Inteligencia: ",self.intelligence)
        print("Defensa: ",self.defense)
        print("Vida: ",self.life)

    #Metodo que nos permite subir de nivel
    def subir_nivel(self, fuerza, inteligencia, defensa, vida):
        self.strength= self.strength + fuerza
        self.intelligence= self.intelligence + inteligencia
        self.defense= self.defense + defensa
        self.life= self.life + vida

    #Metodo que determine si el personaje esta vivo o muerto
    def esta_vivo(self):
        return self.life>0

    # Metodo morir
    def morir(self):
        self.life=0
        print(f"{self.name} esta muerto")

    # Metodo de daño que realizo al enemigo
    def daño(self, enemigo):
        return self.strength- enemigo.defense
        #return f"El daño causado por {self.name} es de {self.strength- enemigo.defense} al rival {enemigo.name}"


    # Ataque
    def atacar(self,enemigo):
        daño=self.daño(enemigo)
        enemigo.life=enemigo.life - daño
        print(f"{self.name} ha realizado {daño} puntos de daño al rival {enemigo.name}")
        if not enemigo.esta_vivo():
            enemigo.morir()
        print(enemigo.life)

    def combate(self,enemigo):
        while self.esta_vivo():
            self.atacar(enemigo)
            while enemigo.esta_vivo():
                enemigo.atacar(self)
                esle:
                break


    
# Herencia
class Guerrero(Personaje):
    def __init__(self, name, strength, intelligence, defense, life,espada):
        suer().__init__(nombre, fuerza, inteligencia, defensa, vida,espada) #Le estoy diciendo que tome estas definiciones de la clase padre
        self.sword= espada



# #Instanciar un objeto de la clase Personaje
daniel=Personaje("Daniel",90,120,45,600)
facundo=Personaje("Facundo", 95, 115, 0, 13)
daniel.atributos()
print("\n")
facundo.atributos()
# print("\n\n")
# # Llamo al metodo subir nivel
# # daniel.subir_nivel(100,30,15,-1150)
# # daniel.atributos()
# print("\n\n")
# # Llamo al metodo esta vivo
# print("esta vivo" if daniel.esta_vivo() else "esta muerto")

# daniel.morir()




print(daniel.daño(facundo))
daniel.atacar(facundo)
