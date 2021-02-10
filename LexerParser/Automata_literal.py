    #Variables auxiliares
TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"


    #Función transición
def delta(state, caracter):
    #{q0, "’" , q1}
    if state == 0 and caracter == "’":
        return 1

    #{q1, "’" , qf}
    if state == 1 and caracter == "’":
        return 2

    #{q1, "números" , q1}
    if state == 1 and caracter.isdigit() == True:
        return 1

    #{q1, "letras" , q1}
    if state == 1 and caracter.isalpha() == True:
        return 1

    #{q1, " " , q1}
    if state == 1 and caracter == " ":
        return 1

    return TRAP_STATE


    #Autómata literal
def automata_literal(input):
    state = 0
    final = 2
        
    for caracter in input:
        next_state = delta(state, caracter)
        #print(("transicion", state, caracter, next_state))
        state = next_state

    if state == final:
        #print(input, "pertenece al lenguaje")
        return RESULT_ACCEPTED

    if state != TRAP_STATE:
        #print(input, "aún no pertenece al lenguaje")
        return RESULT_NOT_ACCEPTED

    #print(input, "no pertenece al lenguajes")
    return RESULT_TRAP


    #Tests
#assert(automata_literal("’hola") == RESULT_TRAP)
#print(" ")
#assert(automata_literal("’’") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_literal("99-88") == RESULT_TRAP)
#print(" ")
#assert(automata_literal("’UTN Facultad Regional Delta’") == RESULT_ACCEPTED)