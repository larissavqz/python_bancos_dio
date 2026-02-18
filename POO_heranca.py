class Veiculo ():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        return f"{self.ano} {self.marca} {self.modelo}"
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def exibir_informacoes(self):
        info_veiculo = super().exibir_informacoes()
        return f"{info_veiculo}, Portas: {self.portas}"
    

# Exemplo de uso
meu_carro = Carro("Toyota", "Corolla", 2020, 4)
print(meu_carro.exibir_informacoes())