class Pessoa: #escrita camel case
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())

#Classe vc cria seus tipos personalisados

#Metodo é uma função que pertence a uma Classe, portanto, sempre está conectada a um objeto