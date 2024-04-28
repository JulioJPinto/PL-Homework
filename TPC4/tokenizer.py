import sys
import ply.lex as lex

reserved = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'and': 'AND',
    'or': 'OR',
    'like': 'LIKE',
    'inner': 'INNER',
    'outer': 'OUTER',
}

tokens = [
    'FIELD',
    'COMMAND',
    'DELIMITER',
    'FINAL_DELIMITER',
    'NUMBER',
    'MATH_OPERATOR',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MOREOREQUAL',
    'LESSOREQUAL',
    'MORE',
    'LESS',
] + list(reserved.values())


t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MOREOREQUAL = r'>='
t_LESSOREQUAL = r'<='
t_MORE = r'>'
t_LESS = r'<'

def t_COMMAND(t):
    r'\b[a-zA-Z]+\b'
    to_lower = t.value.lower()
    t.type = reserved.get(to_lower, 'COMMAND') if to_lower in reserved else 'FIELD'
    return t

def t_ATTRIBUTE(t):
    r'\b[a-zA-Z]+\b'
    to_lower = t.value.lower()
    t.type = reserved.get(to_lower, 'ATTRIBUTE') if to_lower in reserved else 'ATTRIBUTE'
    return t

def t_NUMBER(t):
    r'\d+[.]?\d*'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t,;'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def main(stdin):
    lexer = lex.lex()
    
    for line in stdin:
        lexer.input(line)
        for token in lexer:
            if not token: break
            print(token)

if __name__ == "__main__":
    main(sys.stdin)
