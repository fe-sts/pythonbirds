class Pessoa:  # escrita camel case
    def __init__(self, *filhos, nome=None, idade=34):  # criando Parametro (nome, idade)
        self.idade = idade
        self.nome = None  # nome é o Atributo
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    felipe = Pessoa(nome='Felipe')
    karina = Pessoa(felipe, nome='Karina')
    print(Pessoa.cumprimentar(karina))
    print(id(karina))
    print(karina.cumprimentar())
    print(karina.nome)
    print(karina.idade)
    for filho in karina.filhos:
        print(filho.nome)
    print(karina.filhos)
    karina.sobrenome = 'Tanimoto' #Criando Atributo Dinâmico
    print(karina.sobrenome)


# Classe vc cria seus tipos personalisados

# Metodo é uma função que pertence a uma Classe, portanto, sempre está conectada a um objeto
