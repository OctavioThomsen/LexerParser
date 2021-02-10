    #Variables auxiliares
TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"


    #Función transición
def delta(state, caracter):
    #{q0, : , q1}
    if state == 0 and caracter == ":":
        return 1
    
    #{q1, = , qf}
    if state == 1 and caracter == "=":
        return 2
    
    return TRAP_STATE


    #Autómata dosPuntosIgual
def automata_dosPuntosIgual(input):
    state = 0
    final = 2
    
    for caracter in input:
        next_state = delta(state, caracter)
        #print(("transicion", state, caracter, next_state))
        state= next_state
        
    if state == final:
        #print(input, "pertenece al lenguaje")
        return RESULT_ACCEPTED

    if state != TRAP_STATE:
        #print(input, "aún no pertenece al lenguaje")
        return RESULT_NOT_ACCEPTED
    
    #print(input, "no pertence al lenguaje")
    return RESULT_TRAP


    #Tests
#assert(automata_dosPuntosIgual(":") == RESULT_NOT_ACCEPTED)
#print(" ")
#assert(automata_dosPuntosIgual(":=")== RESULT_ACCEPTED)
#print(" ")
#assert(automata_dosPuntosIgual("::::=====") == RESULT_TRAP)