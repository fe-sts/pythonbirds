class Pessoa: #escrita camel case
    def __init__(self,nome = None, idade = 34 ): #criando Parametro (nome, idade)
        self.idade = idade
        self.nome = None   #nome é o Atributo
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Karina')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Felipe Rina'
    print(p.nome)
#Classe vc cria seus tipos personalisados

#Metodo é uma função que pertence a uma Classe, portanto, sempre está conectada a um objeto