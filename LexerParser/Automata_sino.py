    #Variables auxiliares
TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"


    #Función transición
def delta(state, caracter):
    #{q0, "s" , q1}
    if state == 0 and caracter== "s":
        return 1
    
    #{q1, "i" , q2}
    if  state == 1 and caracter == "i":
        return 2
    
    #{q2, "n" , q3}
    if state == 2 and  caracter == "n":
        return 3
    
    #{q3, "o" , q4f}
    if state == 3 and  caracter == "o":
        return 4
    
    return TRAP_STATE
    
    
    #Autómata sino
def automata_sino(input):
    state = 0
    final = 4
        
    for caracter in input:
        next_state = delta(state, caracter)
        #print(("transicion", state, caracter, next_state))
        state = next_state

    if state == final:
        #print( input, "pertenece al lenguajes")
        return RESULT_ACCEPTED
        
    if state != TRAP_STATE:
        #print (input, "aun no pertenece al lenguaje")
        return RESULT_NOT_ACCEPTED
    
    #print (input, "no pertence al lenguje")
    return RESULT_TRAP


    #Tests
#assert (automata_sino("sino") == RESULT_ACCEPTED)
#print(" ")
#assert(automata_sino("si") == RESULT_NOT_ACCEPTED)
#print(" ")
#assert (automata_sino("sssSno") == RESULT_TRAP)