# TPC4: 

### Data: 07/03/2024
### Autor: Júlio Pinto A100742

---

### Resumo
O propósito deste exercício prático era desenvolver um tokenizador básico de SQL utilizando a biblioteca PLY do Python. O programa recebe um trecho de código SQL via STDIN e mostra os tokens identificados juntamente com sua categorização.

Neste exercício tinhamos como objetivo criar um _tokenizer_ básico de SQL utilizando a biblioteca `ply` de Python.

Este programa recebe o código SQL através do _standard input_ e devolve os tokens que identifica, juntamente com a sua categorização.

Utilizando o ficheiro `test.txt` obtive o seguinte resultado:

```sh
> cat test.txt | python3 tokenizer.py
LexToken(SELECT,'Select',1,0)
LexToken(FIELD,'id',1,7)
LexToken(FIELD,'nome',1,11)
LexToken(FIELD,'salario',1,17)
LexToken(FROM,'From',1,25)
LexToken(FIELD,'empregados',1,30)
LexToken(WHERE,'Where',1,41)
LexToken(FIELD,'salario',1,47)
LexToken(MOREOREQUAL,'>=',1,55)
LexToken(NUMBER,820,1,58)
```