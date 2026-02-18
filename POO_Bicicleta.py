class Bicicleta:
    #init - método construtor - é chamado
    # automaticamente quando um objeto é criado
    def __init__(self, cor, modelo, ano, valor):
        #self é um atributo da classe Bicicleta, 
        #significa que estamos nos referindo ao objeto que 
        # está sendo criado, é necessário para acessar 
        # os atributos e métodos da classe.
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # métodos - o primeiro param é sempre self, 
    # independente se for usado ou não e 
    # independente do nome que se dê a esse parâmetro.

    def buzinar(self):
        print("Biiiiiiiii")
    
    def parar(self):
        print("A bicicleta parou")
    
    def acelerar(self):
        print("A bicicleta acelerou")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    # método destrutor - é chamado quando o objeto
    # é deletado ou quando o programa termina
    def __del__(self):
        print(f"O objeto {self.modelo} foi deletado")
        
        
caloi = Bicicleta("vermelha", "caloi 10", 1998, 500)
print(caloi.cor)

caloi.buzinar()
caloi.acelerar()
caloi.parar()

print(caloi)

    