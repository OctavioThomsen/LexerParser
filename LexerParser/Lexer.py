    #Archivos importados
from Automata_aceptar import *
from Automata_coma import *
from Automata_abrPar import *
from Automata_cerPar import *
from Automata_dosPuntosIgual import *
from Automata_entonces import *
from Automata_hacer import *
from Automata_id import *
from Automata_mientras import *
from Automata_mostrar import *
from Automata_numeros import *
from Automata_op import *
from Automata_abrCor import *
from Automata_cerCor import *
from Automata_punto import *
from Automata_puntoYcoma import *
from Automata_si import *
from Automata_sino import *
from Automata_literal import *


    #Automatas
TOKEN_CONFIG = [
    ("num", automata_num),
    ("op", automata_op),
    ("lit", automata_literal),
    ("aceptar", automata_aceptar),
    ("hacer", automata_hacer),
    ("entonces", automata_entonces), 
    ("mientras", automata_mientras),
    ("mostrar", automata_mostrar), 
    ("si", automata_si),
    ("sino", automata_sino), 
    (";", automata_puntoYcoma),
    (":=", automata_dosPuntosIgual),
    ("[", automata_abrCor), 
    ("]", automata_cerCor), 
    ("(", automata_abrPar),
    (")", automata_cerPar),
    (",", automata_coma), 
    (".", automata_punto), 
    ("id", automata_id),
    ]


    #Función candidatos
def calcCandidates(input, candidates):
  allTrapped = True
  candidates = []

  for (tokenKind, automata) in TOKEN_CONFIG:
    res = automata(input)

    if res == RESULT_ACCEPTED:
        allTrapped = False
        candidates.append(tokenKind)

    if res == RESULT_NOT_ACCEPTED:
        allTrapped = False

  return (allTrapped, candidates)


    #Función lexer
def lex(input):
    #Agregamos un espacio al final para facilitar la condicion de corte
    input = input + " "
    index = 0
    tokens = []

        #Comienzo del ciclo
    while index < len(input):
        if input[index] == " ":
            index += 1
            continue

        candidates = []
        start = index

        while True:
            next = calcCandidates(input[start:index + 1], candidates)
            if next[0] == True:
                break

            candidates = next[1]
            index += 1      

            #Error
        if len(candidates) == 0:
            raise Exception("Error: Token desconocido")

            #Token candidato agregado
        tokenKind = candidates[0]
        lexeme = input[start:index]
        token = (tokenKind, lexeme)
        tokens.append(token)

        #Token final
    end_tokenKind = "EOF"
    end_lexeme = "EOF"
    end_token = (end_tokenKind, end_lexeme)
    tokens.append(end_token)
#   print(" ")
#   print("Lista de tokens:")
#   print(tokens)

    return tokens


    #Tests
#print("Test 1:")
#assert(lex("24+3") == [("num","24"),("op","+"),("num","3"),("EOF","EOF")])
#print(" ")

#print("===================================================================")

#print("Test 2:")
#assert(lex("x>=2") == [("id","x"),("op",">="),("num","2"),("EOF","EOF")])
#print(" ")

#print("===================================================================")

#print("Test 3:")
#assert(lex("entonces") == [("entonces", "entonces"),("EOF","EOF")])
#print(" ")

#print("===================================================================")

#print("Test 4:")
#assert(lex(":=") == [(":=",":="),("EOF","EOF")])
#print(" ")

#print("===================================================================")

#print("Test 5:")
#assert(lex("[2*3]") == [("[","["),("num","2"),("op","*"),("num","3"),("]","]"),("EOF","EOF")])
#print(" ")

#print("===================================================================")

#print("Test 6:")
#assert(lex("asd123 mostrar") == [("id","asd123"),("mostrar","mostrar"),("EOF","EOF")])
#print(" ")

#print("===================================================================")

#print("Test 7:")
#assert(lex("abc") == [("id","abc"),("EOF","EOF")])
#print(" ")

#print("===================================================================")

#print("Test 8:")
#assert(lex("9!=5") == [("num","9"),("op","!="),("num","5"),("EOF","EOF")])
#print(" ")

#print("===================================================================")

#print("Test 9:")
#assert(lex("or") == [("op","or"),("EOF","EOF")])
#print(" ")

#print("===================================================================")

#print("Test 10:")
#assert(lex("Test25000 ’Pablito clavó un clavito’ ( aceptar ) 99.525/:=6") == [("id","Test25000"),("lit", "’Pablito clavó un clavito’"),("(","("),("aceptar","aceptar"),(")",")"),("num","99.525"),("op","/"),(":=",":="),("num","6"),("EOF","EOF")])
#print(" ")

#print("===================================================================")

#print("Test 11:")
#assert(lex("’hola francisco’") == [("lit", "’hola francisco’"),("EOF","EOF")])
#print(" ")