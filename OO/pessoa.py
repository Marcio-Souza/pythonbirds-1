class Pessoa:
    def __init__(self, *filho, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filho = list(filho)

    def cumprimentar(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    marcio = Pessoa(nome='Márcio', idade=45)
    mauro = Pessoa(nome='Mauro', idade=47)
    ailton = Pessoa('Ailton', 73)
    ailton.filho = mauro, marcio
    print(marcio.nome, marcio.idade)
    print(mauro.nome, mauro.idade)
    print(Pessoa.cumprimentar(mauro))
    print(marcio.cumprimentar())
    for filhos in ailton.filho:
        print(f'{filhos.nome} {filhos.idade}')
