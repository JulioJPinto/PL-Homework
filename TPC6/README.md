# TPC6: Desenvolvimento de uma GIC

### 1/4/2024
### Autor: Júlio Pinto A100742

## Resumo
Este trabalho tem como principal objetivo o desenvolvimento de uma GIC simples para a seguinte linguagem de programação:

```
?a
b = a*2 / (27-3)
!a+b
c = a*b / (a/b)
```

## Implementação
```
T =  {'?', '!', '=', '+', '-', '*', '/', '(', ')', id, num}

N = {S, Exp1, Exp2, Exp3, Op1, Op2}

S = S

P = {

    S -> '?' id               LA = {'?'}
      | '!' Exp1              LA = {'!'}
      | id '=' Exp1           LA = {id}

    Exp1 -> Exp2 Op1          LA = {'(', num, id}

    Op1 -> '+' Exp1           LA = {'+'}
        | '-' Exp1            LA = {'-'}
        | &                   LA = {')', $}

    Exp2 -> Exp3 Op2          LA = {'(', num, id}

    Op2 -> '*' Exp2           LA = {'*'}
        | '/' Exp2            LA = {'/'}
        | &                   LA = {'+', '-', ')', $}

    Exp3 -> '(' Exp1 ')'      LA = {'('}
        | num                 LA = {num}
        | id                  LA = {id}

}
```