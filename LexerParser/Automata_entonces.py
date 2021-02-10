    #Variables auxiliares
TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"


    #Función transición
def delta(state, caracter):
    #{q0, e , q1}
    if state == 0 and caracter == "e":
        return 1
    
    #{q1, n , q2}
    if state == 1 and caracter == "n":
        return 2
    
    #{q2, t , q3}
    if state == 2 and caracter == "t":
        return 3
    
    #{q3, o , q4}
    if state == 3 and caracter == "o":
        return 4
    
    #{q4, n , q5}
    if state == 4 and caracter == "n":
        return 5
    
    #{q5, c , q6}
    if state == 5 and caracter == "c":
        return 6
    
    #{q6, e , q7}
    if state == 6 and caracter == "e":
        return 7
    
    #{q7, s , qf}
    if state == 7 and caracter == "s":
        return 8
    
    return TRAP_STATE
    
    
    #Autómata entonces
def automata_entonces(input):
    state = 0
    final = 8
        
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
    
    #print (input, "no pertenece al lenguaje")
    return RESULT_TRAP


    #Tests
#assert(automata_entonces("entonces") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_entonces("enton") == RESULT_NOT_ACCEPTED)
#print(" ")
#assert(automata_entonces("enTONCES") == RESULT_TRAP)
#print(" ")
#assert(automata_entonces("EnToNcEs") == RESULT_TRAP)