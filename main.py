import math
import random

class Pokemon:
    def __init__(self, nombre: str, genero: str, dano: int, defensa: int, vida: int):
        self.__nombre = nombre
        self.__genero = genero
        self.__vida = vida
        self.__dano = dano
        self.__defensa = defensa

    # getters
    def getNombre(self):
        return self.__nombre

    def getVida(self):
        return self.__vida

    def getDano(self):
        return self.__dano

    def getDefensa(self):
        return self.__defensa

    # setters
    def setVida(self, vida):
        self.__vida = vida

    def setDano(self, dano):
        self.__dano = dano

    def setDefensa(self, defensa):
        self.__defensa = defensa

    #

    def atacar(self):
        pass

    def defender(self):
        self.setDefensa(self.getDefensa() + 15)

class Ataque:
    def __init__(self, nombre, dmg, velocidad):
        self.__nombre = nombre
        self.__velocidad = velocidad
        self.__dmg = dmg

    def getNombre(self):
        return self.__nombre

    def getDmg(self):
        return self.__dmg

    def getVelocidad(self):
        return self.__velocidad

        

class Planta(Pokemon):
    def __init__(self, nombre, genero, dano, defensa, vida):
        super().__init__(nombre, genero, dano, defensa, vida)
        self.__vida = math.floor(vida * (1 + random.random()))
        self.__tipo = 'planta'
        self.__fuerteContra = 'agua'
        self.__debilContra = 'fuego'

    def getTipo(self):
        return self.__tipo

    def atacar(self):
        atk = Ataque('Latigo Cepa', 80, 80)
        return atk


class Fuego(Pokemon):
    def __init__(self, nombre, genero, dano, defensa, vida):
        super().__init__(nombre, genero,dano, defensa, vida)
        self.__dano = math.floor(dano * (1.2 + random.random()))
        self.__tipo = 'fuego'
        self.__fuerteContra = 'planta'
        self.__debilContra = 'agua'

    def getTipo(self):
        return self.__tipo

    def atacar(self):
        atk = Ataque('Brasas', 80, 100)
        return atk

class Agua(Pokemon):
    def __init__(self, nombre , genero, dano, defensa, vida):
        super().__init__(nombre, genero, dano, defensa, vida)
        self.__tipo = 'fuego'
        self.__defensa = math.floor(defensa * (2 + random.random()))
        self.__fuerteContra = 'planta'
        self.__debilContra = 'agua'

    def getTipo(self):
        return self.__tipo

    def atacar(self):
        atk = Ataque('Chorro de Agua', 100, 90)
        return atk

class Pelea:
    def pelear(self, pokemonUno, pokemonDos):
        while pokemonUno.getVida() > 0 and pokemonDos.getVida() > 0:
            print("Pokemon 1:")
            print("Tipo: " + str(pokemonUno.getTipo()))
            print("Vida:" + str(pokemonUno.getVida()) + ' - Daño: '+ str(pokemonUno.getDano()) + ' - Defensa:' + str(pokemonUno.getDefensa()) + '\n')

            print("Pokemon 2:")
            print("Tipo: " + str(pokemonDos.getTipo()))
            print("Vida:" + str(pokemonDos.getVida()) + ' - Daño: '+ str(pokemonDos.getDano()) + ' - Defensa:' + str(pokemonDos.getDefensa()) + '\n')

            #
            print("Ingrese accion del jugador uno")
            print("1.Atacar  2.Defender")

            entradaUno = input()
            while not (entradaUno == '1' or entradaUno == '2'):
                print('Entrada invalida')
                print("Ingrese accion del jugador uno")
                print("1.Atacar  2.Defender")

                entradaUno = input()
            self.entradaUno = entradaUno

            print("Ingrese accion del jugador dos")
            print("1.Atacar  2.Defender")

            entradaDos = input()
            while not (entradaDos == '1' or entradaDos == '2'):
                print('Entrada invalida')
                print("Ingrese accion del jugador dos")
                print("1.Atacar  2.Defender")

                entradaDos = input()
            self.entradaDos = entradaDos


            if(pokemonUno.atacar().getVelocidad() > pokemonDos.atacar().getVelocidad()):
                print(pokemonUno.getNombre() + " utilizo " + pokemonUno.atacar().getNombre())
                pokemonDos.setVida(pokemonDos.getVida() - (pokemonUno.atacar().getDmg() - (pokemonDos.getDefensa() / 2) ) )

                if(pokemonDos.getVida() > 0):
                    print(pokemonDos.getNombre() + " utilizo " + pokemonDos.atacar().getNombre())
                    pokemonUno.setVida(pokemonUno.getVida() - (pokemonDos.atacar().getDmg() - (pokemonUno.getDefensa() / 2)))
            else:
                print(pokemonDos.getNombre() + " utilizo " + pokemonDos.atacar().getNombre())
                pokemonUno.setVida(pokemonUno.getVida() - (pokemonDos.atacar().getDmg() - (pokemonUno.getDefensa())))

                if(pokemonUno.getVida() > 0):
                    print(pokemonDos.getNombre() + " utilizo " + pokemonDos.atacar().getNombre())
                    pokemonDos.setVida(pokemonDos.getVida() - (pokemonUno.atacar().getDmg() - (pokemonDos.getDefensa())))


        if pokemonUno.getVida() > 0:
            print(pokemonDos.getNombre() + ' se debilito ! El ganador es ' + pokemonUno.getNombre())
        else:
            print(pokemonUno.getNombre() + ' se debilito ! El ganador es ' + pokemonDos.getNombre())

pokeUno = Fuego('Charmander', 'macho', 200, 150, 200)
pokeDos = Agua('Squirtle', 'macho', 250, 50, 200)

pelea = Pelea().pelear(pokeUno, pokeDos)