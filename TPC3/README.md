# TPC2: 

### Data: 27/02/2024
### Autor: Júlio Pinto A100742

---

### Resumo

Neste exercício tinhamos como objetivo criar um pequeno somador de números que se encontre no meio de um texto. 

Os números só serão válidos caso se encontrem entre um ocorrência da palavra `on` e uma occorrência da palavra `off`. Caso encontre `=` este somára todos os valores entre os vários grupos `on` e  `off` que vieram antes deste.

De maneira a conseguir resolver este problema utilizei o módulo `re` para Regex em Python. Pode encontrar a solução no ficheiro `onoff.py` onde utilizo a função `sub` para fazer algumas transformações.

Utilizando o ficheiro `test.txt` obtive o seguinte resultado:

```sh
> cat test.txt | python3 onoff.py

Soma: 3
Soma: 5
```
