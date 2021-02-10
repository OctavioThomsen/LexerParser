    #Variables auxiliares
TRAP_STATE = -1
RESULT_TRAP = "RESULT_TRAP"
RESULT_ACCEPTED = "ACCEPTED"
RESULT_NOT_ACCEPTED = "NOT ACCEPTED"


    #Función transición
def delta(state, caracter):
    #{q0, "m" , q1}
    if state == 0 and caracter == "m":
        return 1
    
    #{q1, "i" , q2}
    if state == 1 and caracter == "i":
        return 2
    
    #{q2, "e" , q3}
    if state == 2 and caracter == "e":
        return 3
    
    #{q3, "n" , q4}
    if state == 3 and caracter == "n":
        return 4
    
    #{q4, "t" , q5}
    if state == 4 and caracter == "t":
        return 5
    
    #{q5, "r" , q6}
    if state == 5 and caracter == "r":
        return 6
    
    #{q6, "a" , q7}
    if state == 6 and caracter == "a":
        return 7
    
    #{q7, "s" , qf}
    if state == 7 and caracter == "s":
        return 8
    
    return TRAP_STATE
    

    #Autómata mientras
def automata_mientras(input):
    state = 0
    final = 8
        
    for caracter in input:
        next_state = delta(state, caracter)
        #print(("transicion", state, caracter, next_state))
        state = next_state

    if state == final:
        #print( input, "pertenece a la cadena")
        return RESULT_ACCEPTED
        
    if state != TRAP_STATE:
        #print(input, "aun no pertenece al lenguaje")
        return RESULT_NOT_ACCEPTED
    
    #print (input, "no pertenece al lenguaje")
    return RESULT_TRAP


    #Tests
#assert (automata_mientras("mientras") == RESULT_ACCEPTED)
#print(" ")
#assert (automata_mientras("mient") == RESULT_NOT_ACCEPTED)
#print(" ")
#assert (automata_mientras("MienTRa") == RESULT_TRAP)