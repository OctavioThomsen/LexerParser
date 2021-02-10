    #Variables auxiliares
TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"


    #Función transición
def delta(state, caracter):
    #{q0, "h" , q1}
    if state == 0 and caracter == "h":
        return 1
    
    #{q1, "a" , q2}
    if state == 1 and caracter == "a":
        return 2
    
    #{q2, "c" , q3}
    if state == 2 and caracter == "c":
        return 3
    
    #{q3, "e" , q4}
    if state == 3 and caracter == "e":
        return 4
    
    #{q4, "r" , qf}
    if state == 4 and caracter == "r":
        return 5
    
    return TRAP_STATE
    

    #Autómata hacer
def automata_hacer (input):
    state = 0
    final = 5
        
    for caracter in input:
        next_state = delta(state, caracter)
        #print(("transicion", state, caracter, next_state))
        state = next_state

    if state == final:
       #print(input, "pertence al lenguaje")
       return RESULT_ACCEPTED
        
    if state != TRAP_STATE:
        #print(input, "aun no pertence al lenguaje")
        return RESULT_NOT_ACCEPTED
    
    #print (input, "no pertenece al lenguaje")
    return RESULT_TRAP


    #Tests
#assert (automata_hacer("hacer") == RESULT_ACCEPTED)
#print(" ")
#assert (automata_hacer("hac") == RESULT_TRAP)
#print(" ")
#assert (automata_hacer("acer") == RESULT_TRAP)
#print(" ")
#assert (automata_hacer ("HACer") == RESULT_TRAP)