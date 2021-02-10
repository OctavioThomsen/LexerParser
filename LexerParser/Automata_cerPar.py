    #Variables auxiliares
TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"


    #Función transición
def delta(state, caracter):
    #{q0, "(" , q1}
    if state == 0 and caracter == ")":
        return 1

    return TRAP_STATE


    #Autómata cerrar Parentesis
def automata_cerPar(input):
    state = 0
    final = 1
        
    for caracter in input:
        next_state = delta(state, caracter)
        #print(("transicion", state, caracter, next_state))
        state = next_state

    if state == final:
        #print(input, "pertence al lenguaje")
        return RESULT_ACCEPTED
   
    #print (input, "no pertence al lenguaje")
    return RESULT_TRAP


    #Tests
#assert(automata_cerPar(")") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_cerPar("(") == RESULT_TRAP)
#print(" ")
#assert(automata_cerPar("()")== RESULT_TRAP)
#print(" ")
#assert(automata_cerPar("")))))))") == RESULT_TRAP)