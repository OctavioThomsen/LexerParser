    #Variables auxiliares
TRAP_STATE = -1
RESULT_TRAP = "RESULT TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"


    #Función transición
def delta(state, caracter):
    #{q0, "a" , q1}
    if state == 0 and caracter == "a":
        return 1
    
    #{q1, "c" , q2}
    if state == 1 and caracter == "c":
        return 2
    
    #{q2, "e" , q3}
    if state == 2 and caracter == "e":
        return 3
    
    #{q3, "p" , q4}
    if state == 3 and caracter == "p":
        return 4
    
    #{q4, "t" , q5}
    if state == 4 and caracter == "t":
        return 5
    
    #{q5, "a" , q6}
    if state == 5 and caracter == "a":
        return 6
    
    #{q6, "r" , qf}
    if state == 6 and caracter == "r":
        return 7
    
    return TRAP_STATE
    
    
    #Autómata aceptar
def automata_aceptar(input):
    state = 0
    final = 7
        
    for caracter in input:
        next_state = delta(state, caracter)
        #print(("transicion", state, caracter, next_state))
        state = next_state

    if state == final:
        #print(input, "pertence al lenguaje")
        return RESULT_ACCEPTED
        
    if state != TRAP_STATE:
        #print(input, "aún no pertence al lenguaje")
        return RESULT_NOT_ACCEPTED

    #print(input, "no pertenece al lenguaje")
    return RESULT_TRAP


    #Tests
#print(" ")
#assert (automata_aceptar("aceptar") == RESULT_ACCEPTED)
#print(" ")
#assert (automata_aceptar("aaaaceptar") == RESULT_TRAP)
#print(" ")
#assert (automata_aceptar("acep") == RESULT_NOT_ACCEPTED)