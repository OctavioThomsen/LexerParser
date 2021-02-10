from Lexer import *

# main data structure
producciones = {
    "Programa": [
        ["Declaracion", ";", "Sentencia"],
        ["Sentencia"],
    ],

    "Declaracion": [
        ["Sentencia", "Declaracion_prima"],
    ],

    "Declaracion_prima": [
        [";", "Declaracion", "Declaracion_prima"],
        [],
    ],

    "Sentencia": [
        ['id', ':=', 'Expresion', 'Sentencia_prima'],
        ['si', 'Expresion', 'entonces', 'Sentencia',
            'sino', 'Sentencia', 'Sentencia_prima'],
        ['si', 'Expresion', 'entonces', 'Sentencia', 'Sentencia_prima'],
        ['mientras', 'Expresion', 'hacer', 'Sentencia', 'Sentencia_prima']
    ],

    "Sentencia_prima": [
        [";", "Sentencia", "Sentencia_prima"],
        [],
    ],

    "Expresion": [
        ["lit", "Expresion_prima"],
        ["num", "Expresion_prima"],
        ["id", "Expresion_prima"],
        ["aceptar", "lit", "id", "Expresion_prima"],
        ["mostrar", "lit", "ListaIdentificadores", "Expresion_prima"],
    ],

    "Expresion_prima": [
        ["[", "Expresion", "]", "Expresion_prima"],
        ["(", "Expresion", ")", "Expresion_prima"],
        ["op", "Expresion", "Expresion_prima"],
        [],
    ],

    "ListaIdentificadores": [
        ["id", ",", "ListaIdentificadores"],
        ["id"],
    ],
}

no_terminales = [
    "Programa",
    "Declaracion",
    "Declaracion_prima",
    "Sentencia",
    "Sentencia_prima",
    "Expresion",
    "Expresion_prima",
    "ListaIdentificadores",
]


def Parser(inputString):
    # internal state
    self = {
        'tokens': lex(inputString),
        'index': 0,
        'error': False,
    }

    # Llamado "algoritmo" en el material
    def parse():
        pni('Programa')
        tokenType_actual = self['tokens'][self['index']][0]
        if tokenType_actual != 'EOF' and self['error']:
            # Cadena no aceptada
            print('Unexpected input termination')
            return False
        # Cadena aceptada
        return True

    def procesar(parteDerecha):
        for simbolo in parteDerecha:
            tokenType = self['tokens'][self['index']][0]
            if simbolo in no_terminales:
                pni(simbolo)
                if self['error']:
                    break
            else:
                if simbolo == tokenType:
                    self['index'] += 1
                else:
                    self['error'] = True
                    break

    # Llamado "Pni" en el material
    def pni(noTerminal):
        for parte_derecha in producciones[noTerminal]:
            self['error'] = False
            pivote_backtracking = self['index']
            procesar(parte_derecha)
            if self['error']:
                # Acá ocurre el backtracking
                self['index'] = pivote_backtracking
            else:
                break

    # La funcion Parser devuelve esto
    return parse()


    # Tests
# Tests1: Programa -> Sentencia
# Sentencia -> id := Expresion Sentencia_prima
#                id     := num
assert Parser("variable := 123") == True

# Sentencia -> si Expresion entonces Sentencia sino Setencia Sentencia_prima
#              si num op num op num entonces    id    := num sino   id     := num
assert Parser("si  2   +  2  ==  4  entonces variable :=  4  sino variable :=  2") == True

# Sentencia -> si Expresion entonces Setencia Setencia_prima
#              si    lit    entonces    id    :=    lit
assert Parser("si ’literal’ entonces variable := ’literal’") == True

# Sentencia -> mientras Expresion hacer Sentencia Sentencia_prima
#              mientras num op id hacer    id    := id
assert Parser("mientras  2  <  n  hacer variable := n") == True

# Sentencia -> id := Expresion Sentencia_prima
#                 id    := num [num op num op num op num] ; si id op num entonces    id    :=     id    sino    id    :=      num
assert Parser("variable :=  2  [ 3  +   4  /   5  +   6 ] ; si n  -   1  entonces variable := variable2 sino variable := 12.0123456789") == True

# Tests2: Programa -> Declaracion ; Sentencia
# Declaracion ; Sentencia -> id := Expresion Sentencia_prima ; id := Expresion Sentencia_prima
#                 id    :=   id      ;    id    :=    lit
assert Parser("variable := variable2 ; variable := ’literal’") == True

# Declaracion ; Sentencia -> si Expresion entonces Sentencia sino Setencia Sentencia_prima ; si Expresion Entonces Sentencia sino Sentencia Sentencia_prima
#              si id  entonces    id    := id  sino    id    :=  id ; si mostrar    lit       id    op num entonces    id    :=  num  sino    id    := num
assert Parser("si ijk entonces variable := ijk sino variable := lmn ; si mostrar ’literal’ variable -   9  entonces variable := 09.99 sino variable := 10") == True

# Declaracion ; Sentencia -> si Expresion entonces Sentencia Sentencia_prima ; id := Expresion Sentencia_prima
#              si    lit    entonces    id    :=    lit    ;    id    :=     num
assert Parser("si ’literal’ entonces variable := ’literal’ ; variable := 12345.54321") == True

# Declaracion ; Sentencia -> mientras Expresion hacer Sentencia Sentencia_prima ; mientras Expresion hacer Sentencia Sentencia_prima
#              mientras mostrar    lit    id , id, id [num op num] hacer    id    :=     lit     ; mientras aceptar    lit        id   op    lit     hacer     id   :=     id
assert Parser("mientras mostrar ’literal’ abc,def,hkh [ 2   +  2 ] hacer variable := ’literales’ ; mientras aceptar ’literal1’ variable - ’literal2’ hacer variable := variable2") == True

# Declaracion ; Sentencia -> si Expresion entonces Sentencia sino Setencia Sentencia_prima ; si Expresion entonces Sentencia Sentencia_prima
#              si num op num entonces mientras id  hacer    id    := num sino     id    :=    id    ; si  aceptar    lit       id    (num op num op num) entonces    id    :=    lit
assert Parser("si  5  >=  5  entonces mientras zxy hacer variable := 321 sino  variable := varible3 ; si  aceptar ’literal’ variable ( 2   *  3  /   4 ) entonces variable := ’literal’") == True
