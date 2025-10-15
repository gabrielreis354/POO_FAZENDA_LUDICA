## Fazenda Lúdica — Revisão dos pilares da Programação Orientada a Objetos (POO)

Este repositório contém um pequeno exercício de revisão dos pilares da POO em Python. O arquivo principal desta pasta é `fazenda_ludica.py`, que implementa uma hierarquia simples de animais e demonstra Encapsulamento, Abstração, Herança e Polimorfismo.

### Sobre `fazenda_ludica.py`

Resumo rápido:

- Define a classe base `Animal` com atributos básicos (`nome`, `idade`) e métodos como `fazer_som()` e `apresentar()`.
- Implementa subclasses: `Cachorro`, `Gato` e `Vaca` que herdam de `Animal` e sobrescrevem (override) métodos para comportamentos específicos.
- A classe `Vaca` usa um atributo privado (`__producao_leite`) e fornece métodos para acessar e atualizar esse valor, ilustrando encapsulamento.
- No bloco `if __name__ == "__main__":` há um exemplo de execução que instancia os animais e demonstra polimorfismo ao iterar sobre uma lista de objetos `Animal`.

Como executar:

Abra um terminal na pasta `revisao_poo` e execute (PowerShell):

```powershell
python fazenda_ludica.py
# ou, se seu sistema usar o launcher do Python:
py -3 fazenda_ludica.py
````

Saída esperada (exemplo):

```text
Olá sou Rex, tenho 5 anos e sou da raça Labrador
Au Au
Olá sou Mimi, tenho 3 anos e sou da raça Siamês
Miauuu
Olá sou Bela, tenho 4 anos e produzo 20 litros de leite por dia
Muuu
Produção de leite: 20 litros por dia
Nova produção de leite: 25 litros por dia
```

### Como o código demonstra os pilares da POO

- Encapsulamento

  - A classe `Vaca` define `__producao_leite` como um atributo privado (name mangling). O acesso e atualização são feitos por métodos (`obter_producao_leite`, `registra_ordenha`) que controlam e validam a alteração do estado.

- Abstração

  - A classe `Animal` define a interface básica (atributos e métodos) que representa o conceito de animal sem expor detalhes de implementação das subclasses.

- Herança

  - `Cachorro`, `Gato` e `Vaca` herdam de `Animal`, reaproveitando atributos comuns (`nome`, `idade`) e estendendo com atributos específicos (por exemplo, `raca` ou produção de leite).

- Polimorfismo
  - As subclasses sobrescrevem `fazer_som()` e `apresentar()`. No exemplo, uma lista heterogênea de `Animal` é iterada e cada objeto executa sua versão do método — comportamento polimórfico.

### Dicas e próximos passos

- Tente adicionar validações nos construtores (ex.: idade >= 0).
- Adicione métodos compartilhados (ex.: `alimentar()`) e veja como as subclasses podem estender ou alterar esse comportamento.
- Escreva testes simples (pytest/unittest) para validar `registra_ordenha` e o comportamento polimórfico.

---

Arquivo: `fazenda_ludica.py`
Propósito: material de revisão e exemplo didático dos pilares da POO em Python.
