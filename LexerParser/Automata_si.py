    #Variable auxiliares
TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"


    #Función transición
def delta(state, caracter):
    #{q0, "s" , q1}
    if state== 0 and caracter == "s":
        return 1
    
    #{q1, "i" , q2f} 
    if state == 1 and caracter == "i":
        return 2
    
    return TRAP_STATE
    
      
    #Autómata si
def automata_si(input):
    state = 0
    final = 2
        
    for caracter in input:
        next_state = delta(state, caracter)
        #print(("transicion", state, caracter, next_state))
        state = next_state

    if state == final:
        #print( input, "pertenece a la lenguaje")
        return RESULT_ACCEPTED

    if state != TRAP_STATE:
        #print(input, "aun no pertenece al lenguaje")
        return RESULT_NOT_ACCEPTED
        
    #print (input, "no pertenece al lenguaje")
    return RESULT_TRAP


    #Tests
#assert (automata_si("si") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_si("s")== RESULT_NOT_ACCEPTED)
#print(" ")
#assert (automata_si("sssiii") == RESULT_TRAP)