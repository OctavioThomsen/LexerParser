    #Variables auxiliares
TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"


    #Función transición
def delta(state, caracter):    
    #Relop
    #{q0, "=" ,q1}
    if state == 0 and caracter == "=":
        return 1

    #{q1, "=", q2f}
    if state == 1 and caracter == "=":
        return 2

    #{q0, ">" ,q3f}
    if state == 0 and caracter == ">":
        return 3

    #{q3, "=" ,q4f}
    if state == 3 and caracter == "=":
        return 4

    #{q0, "<" ,q5f}
    if state == 0 and caracter == "<":
        return 5

    #{q5, "=" ,q6f}
    if state == 5 and caracter == "=":
        return 6

    #{q0, "!" ,q7}
    if state == 0 and caracter == "!":
        return 7

    #{q7, "=" ,q8f}
    if state == 7 and caracter == "=":
        return 8

    #Mulop
    #{q0, "*" ,q9f}
    if state == 0 and caracter == "*":
        return 9

    #{q0, "/" ,q10f}
    if state == 0 and  caracter == "/":
        return 10

    #{q0, "m" ,q11}
    if state == 0 and caracter == "m":
        return 11

    #{q11, "o" ,q12}
    if state == 11 and caracter == "o":
        return 12

    #{q12, "d" ,q13f}
    if state == 12 and caracter == "d":
        return 13

    #{q0, "a" ,q14}
    if state == 0 and caracter == "a":
        return 14

    #{q14, "n" ,q15}
    if state == 14 and caracter == "n":
        return 15

    #{q15, "d" ,q16f}
    if state == 15 and caracter == "d":
        return 16

    #Sumop
    #{q0, "+" ,q17f}
    if state == 0 and caracter == "+":
        return 17

    #{q0, "-" ,q18f}
    if state == 0 and caracter == "-":
        return 18

    #{q0, "o" ,q19}
    if state == 0 and caracter == "o":
        return 19

    #{q19, "r" ,q20f}
    if state == 19 and caracter == "r":
        return 20

    return TRAP_STATE
        

    #Autómata operaciones
def automata_op(input):
    state = 0
    final = [2, 3, 4, 5, 6, 8, 9, 10, 13, 16, 17, 18, 20]
        
    for caracter in input:
        next_state = delta(state, caracter)
        #print(("transicion", state, caracter, next_state))
        state = next_state

    if (state in final):
        #print(input, "pertenece al lenguaje")
        return RESULT_ACCEPTED
        
    if state != TRAP_STATE:
        #print (input, "aun no pertenece al lenguaje")
        return RESULT_NOT_ACCEPTED
    
    #print (input, "no pertenece al lenguaje")   
    return RESULT_TRAP


    #Tests
#print(" ")
#assert(automata_op("test") == RESULT_TRAP)
#print(" ")
#assert(automata_op("123126") == RESULT_TRAP)
#print(" ")
#assert(automata_op("test2") == RESULT_TRAP)
#print(" ")
#assert(automata_op("=") == RESULT_NOT_ACCEPTED)
#print(" ")
#assert(automata_op("==") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_op(">") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_op("<") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_op(">=") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_op("<=") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_op("!") == RESULT_NOT_ACCEPTED)
#print(" ")
#assert(automata_op("!=") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_op("*") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_op("/") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_op("M") == RESULT_TRAP)
#print(" ")
#assert(automata_op("mo") == RESULT_NOT_ACCEPTED)
#print(" ")
#assert(automata_op("mod") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_op("A") == RESULT_TRAP)
#print(" ")
#assert(automata_op("an") == RESULT_NOT_ACCEPTED)
#print(" ")
#assert(automata_op("and") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_op("+") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_op("-") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_op("O") == RESULT_TRAP)
#print(" ")
#assert(automata_op("o") == RESULT_NOT_ACCEPTED)
#print(" ")
#assert(automata_op("or") == RESULT_ACCEPTED)