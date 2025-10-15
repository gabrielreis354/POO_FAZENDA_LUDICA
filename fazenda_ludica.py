class Animal:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def fazer_som(self):
    return "Animal fazendo som"

  def apresentar(self):
    return f"Olá sou {self.nome} e tenho {self.idade} anos"

class Cachorro(Animal):
  def __init__(self, nome, idade, raca):
    super().__init__(nome, idade)
    self.raca = raca

  def fazer_som(self):
    return "Au Au"

  def apresentar(self):
    return f"Olá sou {self.nome}, tenho {self.idade} anos e sou da raça {self.raca}"
  
class Gato(Animal):
  def __init__(self, nome, idade, raca):
    super().__init__(nome, idade)
    self.raca = raca
    
  def fazer_som(self):
    return "Miauuu"
  
  def apresentar(self):
    return f"Olá sou {self.nome}, tenho {self.idade} anos e sou da raça {self.raca}"
  
class Vaca(Animal):
  def __init__(self, nome, idade, producao_leite):
    super().__init__(nome, idade)
    self.__producao_leite = producao_leite  # Atributo privado
    
  def fazer_som(self):
    return "Muuu"
  
  def apresentar(self):
    return f"Olá sou {self.nome}, tenho {self.idade} anos e produzo {self.__producao_leite} litros de leite por dia"

  def obter_producao_leite(self):
    return self.__producao_leite
  
  def registra_ordenha(self, producao):
    if producao >= 0:
      self.__producao_leite = producao
    else:
      print("Produção de leite não pode ser negativa")
      
# Exemplo de uso
if __name__ == "__main__":
  cachorro = Cachorro("Rex", 5, "Labrador")
  gato = Gato("Mimi", 3, "Siamês")
  vaca = Vaca("Bela", 4, 20)

  animais = [cachorro, gato, vaca]

  for animal in animais:
    print(animal.apresentar())
    print(animal.fazer_som())
    if isinstance(animal, Vaca):
      print(f"Produção de leite: {animal.obter_producao_leite()} litros por dia")
      animal.registra_ordenha(25)
      print(f"Nova produção de leite: {animal.obter_producao_leite()} litros por dia")
    print()