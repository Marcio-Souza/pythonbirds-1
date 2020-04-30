class Pessoa:
    _olhos = 2

    def __init__(self, *filho, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filho = list(filho)

    def cumprimentar(self):
        return f'Olá {self.nome}'

class Mutante(Pessoa):
    _olhos = 3

    def cumprimentar(self):
        cumprimento = Pessoa.cumprimentar(self)
        return f'{cumprimento}. Dois pulos'


if __name__ == '__main__':
    marcio = Mutante(nome='Márcio', idade=45)
    mauro = Pessoa(nome='Mauro', idade=47)
    ailton = Pessoa('Ailton', 73)
    ailton.filho = mauro, marcio
    print(marcio.nome, marcio.idade)
    print(mauro.nome, mauro.idade)
    print(Pessoa.cumprimentar(mauro))
    print(marcio.cumprimentar())
    print(marcio._olhos)
    print(mauro._olhos)
    for filhos in ailton.filho:
        print(f'{filhos.nome} {filhos.idade}')
