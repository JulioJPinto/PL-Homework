# TPC1: Análise de dados de Atletas

### Data: 14/02/2024
### Autor: Júlio Pinto A100742

---

### Resumo

Neste exercício foi nos fornecido o dataset `emd.csv`. Este *dataset* contém diversas informações sobre atletas. 

A partir deste *dataset* tinhamos como objetivo conseguir obter os seguintes dados:
- Lista ordenada alfabeticamente das modalidades desportivas;
- Percentagens de atletas aptos e inaptos para a prática desportiva;
- Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...

De maneira a conseguir resolver este problema, sem utilizar o módulo CSV de Python, defini as diferentes funções de *parsing* que poderão ser encontradas no ficheiro `tpc1.py`. Para conseguir obter as estatísticas no mesmo ficheiro defini outras funções como a função `divisions_dist` que permite obter os resultados da distribuição de idades.

Utilizando o ficheiro `tpc1.py` obtive o seguinte *output*:

```py
> cat emd.csv | python3 tpc1.py

Lista de todas as modalidades (Ordem Alfabética):
 - Andebol
 - Atletismo
 - BTT
 - Badminton
 - Basquetebol
 - Ciclismo
 - Dança
 - Equitação
 - Esgrima
 - Futebol
 - Karaté
 - Orientação
 - Parapente
 - Patinagem
 - Triatlo

Número total de atletas: 300
Percentagem de atletas aprovados: 0.54 (162) 
Percentagem de atletas não aprovados: 0.46 (138) 

Distribuição de idades (Intervalos de 5):
20 - 24: 26.666666666666668% (80)
25 - 29: 34.0% (102)
30 - 34: 34.66666666666667% (104)
35 - 39: 4.666666666666667% (14)
```
