""""
    Você deverá criar uma classe Carro que vai possuir dois atributos compostos
    por outras duas classes

    1. Motor
    2. Direçao

    A classe Motor terá a responsabilidade de controlar a velocidade.
    Ele oferece os seguintes atributos:
    1. atributo de dado velocidade
    2. método acelerar que deverá incrementar a velocidade em uma unidade
    3 método frear que deverá decrementar a velocidade em duas unidades

    A classe Direção terá a responsabilidade de controlar a direção. Ela
    oferecerá os seguintes atributos:
    1. Valor da direção com valores possíveis: Norte, Sul, Leste, Oeste
    2. Método girar a direita
    3. Método girar a esquerda

        N
     O     L
        S

    Ex.:
    >>> #teste do Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    # teste da Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> #teste do carro
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
     >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
"""
NORTE = 'Norte'
LESTE = 'Leste'
SUL   = 'Sul'
OESTE = 'Oeste'


class Direcao:
    _girar_direita = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    _girar_esquerda = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self._girar_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self._girar_esquerda[self.valor]


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Carro(Direcao, Motor):

    velocidade = 0

    def __init__(self, direcao, motor):
        super()
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()




if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    direcao = Direcao()
    print(direcao.valor)
    direcao.girar_a_direita()
    print(direcao.valor)

